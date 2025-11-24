import streamlit as st
import pandas as pd
import plotly.express as px
from sentence_transformers import SentenceTransformer, util
from textblob import TextBlob

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Nirmaan AI Scorer",
    page_icon="🎓",
    layout="wide"
)

# --- CUSTOM CSS FOR DASHBOARD UI ---
st.markdown("""
    <style>
    /* Center the main title */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        color: #1E1E1E;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 30px;
    }
    /* Style the Score Card */
    .score-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        margin-top: 20px;
    }
    .score-val {
        font-size: 60px;
        font-weight: 800;
        line-height: 1;
    }
    .score-lbl {
        font-size: 20px;
        font-weight: 500;
        opacity: 0.9;
    }
    /* Style the Input Area */
    .stTextArea textarea {
        font-size: 16px;
        line-height: 1.6;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. LOAD MODELS ---
@st.cache_resource
def load_nlp_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

nlp_model = load_nlp_model()

# --- 2. CORE LOGIC (Rubric aligned) ---
def check_salutation(text):
    lower_text = text.lower()
    if any(x in lower_text for x in ["excited to introduce", "feeling great", "pleasure to meet"]):
        return 5, "Excellent (Enthusiastic)"
    if any(x in lower_text for x in ["good morning", "good afternoon", "good evening", "good day", "hello everyone"]):
        return 4, "Good (Formal)"
    if any(x in lower_text for x in ["hi", "hello", "hey"]):
        return 2, "Normal (Basic)"
    return 0, "No Salutation"

def check_keywords_with_nlp(text):
    sentences = text.split('.')
    must_have = {
        "Name": ["my name is", "myself", "i am"],
        "Age": ["years old", "age is"],
        "School/Class": ["studying in", "class", "grade", "school"],
        "Family": ["family", "parents", "mother", "father"],
        "Hobbies": ["hobby", "hobbies", "playing", "enjoy"]
    }
    good_to_have = {
        "Origin": ["from", "live in"],
        "Ambition": ["goal", "dream", "ambition"],
        "Unique": ["fact", "special", "unique"]
    }
    score = 0
    details = []
    
    # Must Haves (4 pts)
    for category, keywords in must_have.items():
        found = False
        if any(k in text.lower() for k in keywords): found = True
        if not found:
            cat_emb = nlp_model.encode(f"my {category}", convert_to_tensor=True)
            txt_emb = nlp_model.encode(text, convert_to_tensor=True)
            if util.pytorch_cos_sim(txt_emb, cat_emb).item() > 0.35: found = True
        
        if found:
            score += 4
            details.append(f"✅ {category}")
        else:
            details.append(f"❌ {category}")

    # Good to Haves (2 pts)
    for category, keywords in good_to_have.items():
        if any(k in text.lower() for k in keywords):
            score += 2
            details.append(f"✅ {category}")
            
    return min(30, score), ", ".join(details)

def check_flow(text):
    lower = text.lower()
    try:
        s_idx = -1
        for s in ["hello", "hi", "good"]: 
            if s in lower: 
                s_idx = lower.find(s)
                break
        n_idx = lower.find("name") if "name" in lower else lower.find("myself")
        c_idx = lower.find("thank")
        
        if s_idx < n_idx and (c_idx > n_idx or c_idx == -1): return 5, "Good Structure"
        return 2, "Flow needs improvement"
    except: return 0, "Unclear"

def check_speech_rate(word_count, duration):
    if duration <= 0: return 0, "N/A"
    wpm = word_count / (duration / 60)
    if 111 <= wpm <= 140: return 10, f"{int(wpm)} WPM (Ideal)"
    if 81 <= wpm <= 160: return 6, f"{int(wpm)} WPM (Acceptable)"
    return 2, f"{int(wpm)} WPM (Too Fast/Slow)"

def check_grammar(text):
    sentences = [s.strip() for s in text.split('.') if s]
    errors = sum(1 for s in sentences if not s[0].isupper())
    score = max(0, 10 - (errors/len(sentences)*20)) if sentences else 0
    return int(score), f"Score: {int(score)}/10"

def check_fillers(text):
    fillers = ["um", "uh", "like", "so", "actually"]
    words = text.lower().split()
    count = sum(1 for w in words if w in fillers)
    rate = (count/len(words))*100 if words else 0
    if rate <= 3: return 15, "Excellent (<3%)"
    return 9, f"Found {rate:.1f}% fillers"

def check_engagement(text):
    blob = TextBlob(text)
    positivity = (blob.sentiment.polarity + 1) / 2
    if positivity > 0.6: return 15, "High Positivity"
    return 10, "Neutral/Low"

def calculate_final_score(transcript, duration):
    results = []
    # Checks
    s, sm = check_salutation(transcript)
    results.append({"Criterion": "Salutation", "Score": s, "Max": 5, "Feedback": sm})
    
    k, km = check_keywords_with_nlp(transcript)
    results.append({"Criterion": "Keywords", "Score": k, "Max": 30, "Feedback": km})
    
    f, fm = check_flow(transcript)
    results.append({"Criterion": "Flow", "Score": f, "Max": 5, "Feedback": fm})
    
    sr, srm = check_speech_rate(len(transcript.split()), duration)
    results.append({"Criterion": "Pacing", "Score": sr, "Max": 10, "Feedback": srm})
    
    g, gm = check_grammar(transcript)
    results.append({"Criterion": "Grammar", "Score": g, "Max": 10, "Feedback": gm})
    
    c, cm = check_fillers(transcript)
    results.append({"Criterion": "Clarity", "Score": c, "Max": 15, "Feedback": cm})
    
    e, em = check_engagement(transcript)
    results.append({"Criterion": "Engagement", "Score": e, "Max": 15, "Feedback": em})
    
    ttr = len(set(transcript.lower().split())) / len(transcript.split()) if transcript else 0
    v_score = 10 if ttr > 0.6 else 5
    results.append({"Criterion": "Vocabulary", "Score": v_score, "Max": 10, "Feedback": f"TTR: {ttr:.2f}"})

    total = sum(r['Score'] for r in results)
    return total, pd.DataFrame(results)

# --- 3. DASHBOARD UI LAYOUT ---

st.markdown('<div class="main-title">🎓 Nirmaan AI Evaluator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced Communication Skills Assessment System</div>', unsafe_allow_html=True)

# --- SECTION 1: INPUT (Full Width) ---
st.subheader("1. Student Input")
st.info("Paste the speech transcript below for analysis.")

# Input area (Top)
transcript = st.text_area("Transcript Text", value="", height=200, placeholder="Paste the student's transcript here...")

c1, c2, c3 = st.columns([1, 1, 2])
with c1:
    duration = st.number_input("Audio Duration (sec)", value=52, min_value=1)
with c2:
    st.write("") # Spacer to align button
    st.write("") 
    analyze_btn = st.button("✨ GENERATE SCORE REPORT", type="primary", use_container_width=True)

st.markdown("---")

# --- SECTION 2: RESULTS (Full Width, below Input) ---
if analyze_btn:
    if not transcript.strip():
        st.error("⚠️ Please enter a transcript to analyze.")
    else:
        st.subheader("2. Performance Report")
        with st.spinner("🤖 AI is analyzing keywords, sentiment, and flow..."):
            final_score, df_results = calculate_final_score(transcript, duration)
        
        # --- SCORE CARD ---
        st.markdown(f"""
            <div class="score-container">
                <div class="score-lbl">OVERALL PROFICIENCY</div>
                <div class="score-val">{final_score}/100</div>
                <div style="margin-top: 10px; font-size: 18px;">
                    {'🌟 EXCELLENT' if final_score > 80 else '👍 GOOD EFFORT' if final_score > 50 else '⚠️ NEEDS IMPROVEMENT'}
                </div>
            </div>
        """, unsafe_allow_html=True)

        # --- CHART & TABLE ---
        col_chart, col_table = st.columns([1, 1], gap="large")
        
        with col_chart:
            st.markdown("### 📈 Visual Breakdown")
            fig = px.bar(
                df_results, 
                x="Score", 
                y="Criterion", 
                orientation='h',
                text="Score",
                color="Score",
                color_continuous_scale="Blues",
                range_x=[0, 35] 
            )
            fig.update_layout(
                yaxis={'categoryorder':'total ascending'}, 
                xaxis_title="Points", 
                yaxis_title="",
                height=400,
                margin=dict(l=0, r=0, t=0, b=0),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with col_table:
            st.markdown("### 📝 Detailed Feedback")
            
            # --- DYNAMIC HEIGHT CALCULATION ---
            # Standard row height ~35px, Header ~38px. 
            # This ensures the table fits exactly with no extra whitespace.
            rows = len(df_results)
            height_calc = (rows * 35) + 38
            
            st.dataframe(
                df_results[["Criterion", "Score", "Max", "Feedback"]],
                use_container_width=True,
                hide_index=True,
                height=height_calc, # <--- FIXED: Dynamic height based on row count
                column_config={
                    "Score": st.column_config.NumberColumn(format="%d pts"),
                    "Max": st.column_config.NumberColumn(format="%d pts")
                }
            )