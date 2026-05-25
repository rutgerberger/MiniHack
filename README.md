---
Welcome to the first official event of **Calculemus**! Ready to put theory into practice? Bring your laptop and your sharpest ideas, because we are diving straight into building smart solutions with modern AI frameworks. 

Brightspace and scattered course materials can be complex to navigate. This Friday, your mission is to solve that. You and your team will build a **Personalized Study Agent** that takes raw course files and transforms them into a tool that makes a student’s life easier, organized, and highly efficient. 

Pizza, drinks, and competitive action are fully included!

---

## 📅 Schedule (Friday, June 12)
* **13:00 - 13:30** | Walk-in & Proposal of Challenge
* **13:30 - 17:00** | **HACKATHON ALIVE:** Coding, Prompting & Building
* **17:00 - 17:30** | Project Demonstrations
* **17:30 - 18:00+** | Winner Announcement & Celebratory Drinks 🍕🥤

---

## 🚀 The Challenge: Personalized Study Agent
Your goal is to build an AI assistant based on a set of provided university course files. How it helps is entirely up to your team’s imagination. Think of features like:
* Extracting critical deadlines, exam dates, and milestones directly into a calendar.
* Generating interactive practice questions, summaries, or flashcards from lecture slides.
* Building an intelligent search/Q&A tool over complex syllabi.

### ⚠️ Rules & Constraints
To keep the playing field fair and secure, your project must strictly adhere to these rules:
1. **Empower, Don't Cheat:** The tool must make a student *better* or *more efficient* at studying, not lazier. Tools designed to automatically solve graded assignments or cheat will be instantly disqualified.
2. **Safety First:** **No usage of UL (University Leiden) passwords or credentials allowed.** Any hardcoded or handled university login credentials in your repository means immediate disqualification.
3. **Timeline:** Everything must be built within the designated 3.5-hour window.
4. **API Key:** To ensure a fair competition, you are not allowed to use other API keys than the free API key provided by Groq. See https://console.groq.com/docs/rate-limits

---

## 🛠️ What We Provide
Don't worry, you won't have to start from scratch! We will supply a robust **Python framework/starter kit** that includes:
* Baseline code to parse provided course materials into structured formats.
* A simple UI with a pre-configured 'toolkit' connection to hook up your AI agents and components easily.
* Open flexibility: You are free to expand this framework or build your own custom pipeline if your solution requires it.

---

## 🏆 Prizes
We have awesome individual rewards up for grabs for the top team.

---

## 👥 Logistics & Registration
* **Team Size:** 3 to 4 people. You can sign up as a full team, or join individually and we will match you with a team during the walk-in!
* **Capacity:** Limited to a maximum of 20–30 participants. Secure your spot early!
* **Food & Entry:** Pizza and drinks are included. 

### 💻 What to Bring
* Your laptop and charger.
* A working Python environment installed.
* Your creative problem-solving mindset!

---

# 🚀 Technical Docs.

Welcome to the Friday Mini-Hack! This repository contains the **Starter Baseline** to help you hit the ground running. You have 3.5 hours to turn raw university course files into a smart, personalized AI study assistant. 

## 📁 Repository Structure

* `app.py` - The Streamlit frontend. Handles the chat interface and document loading UI.
* `agent.py` - The brain. Connects to the **Groq API** (Llama 3) and handles the AI prompts.
* `document_parser.py` - The extractor. Reads through the `CourseMaterial/` folder and pulls text from PDFs and Markdown files.
* `requirements.txt` - All the necessary Python packages.
* `.env.example` - Template for your API keys (Security first!).
* `CourseMaterial/` - The dataset of Machine Learning lectures, notes, and exercises you will be hacking on.

## 🛠️ Quick Start Guide

Get your baseline running in under 2 minutes:

### 1. Set up a Virtual Environment (Highly Recommended)
Keep your project dependencies clean!
```bash
# Create the environment
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

*(Note: This includes a specific version of `httpx` to prevent compatibility issues with the Groq client!)*

### 3. Add Your Groq API Key

1. Create a new file named exactly `.env` in the root folder.
2. Add your Groq API key to it:

```text
GROQ_API_KEY=gsk_your_api_key_here

```

### 4. Launch the App!

```bash
streamlit run app.py

```

Your browser will automatically open to `http://localhost:8501`. Click **"Load Course Materials"** in the sidebar to parse the data, and start chatting!

## 🧩 Where to Hack? (Extension Points)

This baseline is intentionally basic. Your job is to make it smart! Look for `[HACKATHON EXTENSION POINT]` comments in the code:

* **`document_parser.py`:** Add functions to read the `.ipynb` (Jupyter Notebook) files or `.mat` data files in the Course Materials. Build a smarter "chunking" algorithm so you don't overwhelm the LLM's context window.
* **`app.py`:** Instead of loading the *entire* course into the chat context, build a search function (RAG - Retrieval-Augmented Generation) to only pass the most relevant paragraphs to the AI.
* **`agent.py`:** Tweak the `system_prompt`. Make the agent act as a strict quiz-master, a flashcard generator, or an exam scheduler.

## ⚠️ Hackathon Rules

1. **Empower, Don't Cheat:** Build tools that make students better, not lazier. Tools designed solely to solve graded assignments will be disqualified.
2. **Safety First:** DO NOT use or hardcode University Leiden credentials anywhere. Keep your Groq API keys in the `.env` file and out of your scripts.

Good luck, and may the best Study Agent win! 🍕🏆

Students can team up with 3-4 people.

---
