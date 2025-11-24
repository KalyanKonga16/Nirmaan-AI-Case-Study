# **🎓 Nirmaan AI Communication Evaluator**

## **🚀 Overview**

The **Nirmaan AI Evaluator** is an automated assessment tool designed to analyze student spoken introductions. It combines **Rule-Based Logic** (for structure and pacing) with **NLP Semantic Analysis** (for content relevance) to generate a rubric-aligned proficiency score (0-100).

This tool addresses the Nirmaan Case Study requirement for an automated scoring system that provides granular, actionable feedback.

## **🧠 Scoring Formula & Logic**

The system evaluates transcripts against an 8-point weighted rubric, identical to the case study requirements.

| Criterion | Weight | Scoring Logic |
| :---- | :---- | :---- |
| **1\. Salutation** | **5%** | **Rule-Based:** Checks for formal ("Good morning") vs. enthusiastic ("Excited to be here") vs. basic ("Hi") greetings. |
| **2\. Keywords** | **30%** | **NLP (Semantic):** Uses Cosine Similarity (Sentence-Transformers) to detect key concepts (Name, Family, Hobbies) even if exact words are missing. |
| **3\. Flow** | **5%** | **Structural:** Verifies the logical sequence: *Salutation → Name → Details → Closing*. |
| **4\. Speech Rate** | **10%** | **Math:** Calculates Words Per Minute (WPM). • **Ideal:** 111-140 WPM • **Fast/Slow:** Penalized based on deviation. |
| **5\. Grammar** | **10%** | **Heuristic:** Analyzes sentence capitalization and punctuation structure as a proxy for grammatical correctness. |
| **6\. Vocabulary** | **10%** | **Statistical:** Calculates **Type-Token Ratio (TTR)** to measure lexical diversity (unique words vs total words). |
| **7\. Clarity** | **15%** | **Pattern Matching:** Detects the density of filler words (*um, uh, like, you know*) to assess fluency. |
| **8\. Engagement** | **15%** | **Sentiment Analysis:** Uses **TextBlob** to measure the polarity of the text (Positive/Enthusiastic vs. Neutral/Flat). |

## **🛠️ Tech Stack**

* **Frontend:** Streamlit (Python)  
* **NLP Engine:** sentence-transformers (Model: *all-MiniLM-L6-v2*)  
* **Sentiment Engine:** TextBlob  
* **Data Visualization:** Plotly Express  
* **Data Processing:** Pandas

## **📦 Quick Start (Local)**

1. **Clone the Repository**  
   git clone \[https://github.com/YOUR\_USERNAME/nirmaan-ai-evaluator.git\](https://github.com/YOUR\_USERNAME/nirmaan-ai-evaluator.git)  
   cd nirmaan-ai-evaluator

2. **Install Dependencies**  
   pip install \-r requirements.txt

3. **Run the Application**  
   streamlit run app.py

4. Access the Dashboard  
   Open your browser to http://localhost:8501

## **☁️ Deployment**

For detailed deployment instructions on local servers or cloud platforms, please refer to the [DEPLOYMENT\_GUIDE.md](https://www.google.com/search?q=DEPLOYMENT_GUIDE.md).

## **📂 Repository Structure**

* app.py: The main application source code.  
* requirements.txt: List of Python dependencies.  
* README.md: Project documentation.  
* DEPLOYMENT\_GUIDE.md: Step-by-step setup manual.