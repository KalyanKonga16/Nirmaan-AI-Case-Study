🎓 Nirmaan AI Communication Evaluator

🚀 Overview

The Nirmaan AI Evaluator is an automated assessment tool designed to evaluate student spoken introductions. It combines Rule-Based Logic (for structure and pacing) with NLP Semantic Analysis (for content relevance) to generate a rubric-aligned proficiency score (0-100).

This tool addresses the Nirmaan Case Study requirement for an automated scoring system that provides granular, actionable feedback.

🧠 Scoring Logic (The "Brain" of the App)

The system evaluates transcripts against an 8-point weighted rubric, identical to the case study requirements:

Criterion

Weight

Logic Used

Salutation

5%

Rule-Based: Detects formal vs. enthusiastic greetings.

Keywords

30%

NLP (Cosine Similarity): Detects concepts (Name, Family, Hobbies) even if exact words are missing.

Flow

5%

Structural Logic: Checks sequence (Greeting → Name → Details → Closing).

Speech Rate

10%

Math: WPM calculation based on audio duration (Target: 111-140 WPM).

Grammar

10%

Heuristic: Capitalization and sentence structure checks.

Vocabulary

10%

Statistical: Type-Token Ratio (TTR) for lexical diversity.

Clarity

15%

Pattern Matching: Detection of filler words (um, uh, like).

Engagement

15%

Sentiment Analysis: TextBlob polarity scoring.

🛠️ Tech Stack

Frontend: Streamlit (Python)

NLP Engine: sentence-transformers (all-MiniLM-L6-v2)

Sentiment: TextBlob

Visualization: Plotly Express

📦 Quick Start

For detailed installation steps, please refer to DEPLOYMENT_GUIDE.md.

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
