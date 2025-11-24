# **📘 Deployment & Execution Guide**

This document outlines the exact steps to deploy and run the **Nirmaan AI Evaluator** on a local server or machine.

## **✅ Prerequisites**

Before starting, ensure you have the following installed:

1. **Python 3.9 or higher** ([Download Here](https://www.python.org/downloads/))  
2. **Git** (Optional, for cloning)  
3. **VS Code** or any code editor.

## **🚀 Step 1: Setup the Environment**

1. **Download the Code**  
   * Clone the repository or download the ZIP file.

git clone \[https://github.com/YOUR\_USERNAME/nirmaan-ai-evaluator.git\](https://github.com/YOUR\_USERNAME/nirmaan-ai-evaluator.git)  
cd nirmaan-ai-evaluator

2. **Create a Virtual Environment (Recommended)**  
   * This keeps your dependencies clean.  
   * **Windows:**  
     python \-m venv venv  
     venv\\Scripts\\activate

   * **Mac/Linux:**  
     python3 \-m venv venv  
     source venv/bin/activate

## **📦 Step 2: Install Dependencies**

1. Run the following command to install all necessary AI and UI libraries:  
   pip install \-r requirements.txt

   *Note: The first time you run this, it may take 1-2 minutes to download the NLP models.*

## **▶️ Step 3: Run the Application**

1. Execute the Streamlit server:  
   streamlit run app.py

2. **Access the Dashboard:**  
   * The application will automatically launch in your default web browser.  
   * Local URL: http://localhost:8501

## **🧪 Step 4: Verification (Testing the App)**

1. **Input:** Paste the sample transcript into the text area.  
2. **Duration:** Set duration to 52 seconds.  
3. **Action:** Click the **"✨ GENERATE SCORE REPORT"** button.  
4. **Result:** Verify that the "Overall Proficiency" score appears along with the Bar Chart.

## **☁️ Option 2: Cloud Deployment (Streamlit Community Cloud)**

To make this accessible publicly:

1. Push this code to a public GitHub repository.  
2. Go to [share.streamlit.io](https://share.streamlit.io).  
3. Connect your GitHub account.  
4. Select this repository and click **Deploy**.