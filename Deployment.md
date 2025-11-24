📘 Deployment & Execution Guide
This document outlines the exact steps to deploy and run the Nirmaan AI Evaluator on a local server or machine.
✅ Prerequisites
Before starting, ensure you have the following installed:
Python 3.9 or higher (Download Here)
Git (Optional, for cloning)
VS Code or any code editor.
🚀 Step 1: Setup the Environment
Download the Code
Clone the repository or download the ZIP file.
git clone [https://github.com/YOUR_USERNAME/nirmaan-ai-evaluator.git](https://github.com/YOUR_USERNAME/nirmaan-ai-evaluator.git)
cd nirmaan-ai-evaluator


Create a Virtual Environment (Recommended)
This keeps your dependencies clean.
Windows:
python -m venv venv
venv\Scripts\activate


Mac/Linux:
python3 -m venv venv
source venv/bin/activate


📦 Step 2: Install Dependencies
Run the following command to install all necessary AI and UI libraries:
pip install -r requirements.txt

Note: The first time you run this, it may take 1-2 minutes to download the NLP models.
▶️ Step 3: Run the Application
Execute the Streamlit server:
streamlit run app.py


Access the Dashboard:
The application will automatically launch in your default web browser.
Local URL: http://localhost:8501
🧪 Step 4: Verification (Testing the App)
Input: Paste the sample transcript into the text area.
Duration: Set duration to 52 seconds.
Action: Click the "✨ GENERATE SCORE REPORT" button.
Result: Verify that the "Overall Proficiency" score appears along with the Bar Chart.
☁️ Option 2: Cloud Deployment (Streamlit Community Cloud)
To make this accessible publicly:
Push this code to a public GitHub repository.
Go to share.streamlit.io.
Connect your GitHub account.
Select this repository and click Deploy.
