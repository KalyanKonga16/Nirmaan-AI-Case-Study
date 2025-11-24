# Nirmaan AI Intern Case Study - Automated Communication Scorer

## Overview
This tool evaluates student spoken introductions by combining **Rule-based logic** (keyword matching) and **NLP Semantic Analysis** (Sentence-Transformers) to produce a rubric-driven score.

## Features
- **Hybrid Scoring:** Uses exact keyword matching + semantic cosine similarity.
- **Dynamic Rubric:** Accepts an Excel file to adjust scoring criteria dynamically.
- **Real-time Feedback:** Provides granular feedback per criterion.

## Tech Stack
- **Python 3.10+**
- **Streamlit:** For rapid frontend deployment.
- **Sentence-Transformers (All-MiniLM-L6-v2):** For efficient semantic embedding.
- **Pandas:** For data handling.

## How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt