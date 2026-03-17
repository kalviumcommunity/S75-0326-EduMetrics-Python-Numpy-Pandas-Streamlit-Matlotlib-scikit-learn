📊 EduMetrics

A Data-Driven Academic Feedback Analytics Platform

EduMetrics is a smart analytics platform that transforms raw student feedback into actionable academic insights using data science and machine learning. It enables universities to measure teaching quality, course difficulty, and student satisfaction through an interactive dashboard.

📌 1. Problem Statement & Solution Overview
🔴 Problem

Universities collect large volumes of student feedback every semester. However:

Data is often stored as raw numbers or text

No clear insights are extracted

Trends and patterns remain hidden

Decision-making becomes guesswork

This affects:

Academic administrators

Faculty members

Students (indirectly through poor course improvements)

💡 Solution

EduMetrics solves this by connecting:

Problem → Data → Model → App

📂 Data: Student survey responses (ratings + feedback)

🧠 Model: ML models analyze sentiment and predict risks

📊 App: Streamlit dashboard visualizes insights

👤 User Interaction

Admin uploads CSV dataset

System processes data automatically

Dashboard displays insights, trends, and alerts

📊 2. Dataset Selection & Scope
📂 Dataset

The dataset consists of student feedback with fields like:

course_name

teaching_quality

difficulty

satisfaction

assignment_load

feedback (text)

✅ In Scope

Feedback analysis

Course performance metrics

Sentiment classification

Risk prediction

Visualization of trends

❌ Out of Scope

Real-time data streaming

Deep learning models

Complex NLP (like transformers)

Multi-university comparisons

👉 Focus is on simple, effective ML within sprint limits

👥 3. Roles & Responsibilities
🧠 Data & Preprocessing — Jevin Josh

Data collection and cleaning (Pandas)

Handling missing values

Feature preparation

🤖 ML & Analytics — Abishek

Sentiment analysis (scikit-learn)

Course risk prediction

Course Health Score calculation

📊 Visualization — Jemimah

Charts using Matplotlib

Trend analysis

Insight representation

💻 App Development — Jevin Josh + Abishek

Streamlit dashboard

Integration of ML + visuals

File upload & UI

🔁 Shared (All)

Testing

Debugging

Documentation

Final presentation

📅 4. Sprint Timeline (4 Weeks)
🟢 Week 1 — Data Preparation

Define dataset structure

Clean and preprocess data

Prepare features

🟡 Week 2 — Modeling

Build sentiment analysis model

Create Course Health Score

Implement risk detection

🔵 Week 3 — App Development

Build Streamlit dashboard

Add charts and insights

Integrate ML outputs

🔴 Week 4 — Testing & Deployment

Debugging and UI improvements

Add recommendations and alerts

Prepare README & demo

🚀 5. MVP (Minimum Viable Product)

The MVP includes:

CSV upload feature

Course performance dashboard

Sentiment analysis (basic ML)

Course Health Score

At least 2–3 visualizations

👉 Ensures end-to-end functionality from data → insight

⚙️ 6. Functional Requirements

The system must:

Accept CSV dataset input

Process and clean data

Perform sentiment classification

Calculate course metrics

Display visual insights

Predict course risk levels

Provide recommendations

⚡ 7. Non-Functional Requirements
⏱ Performance

Should process dataset within seconds

🔒 Reliability

Handle missing or incorrect inputs

🎯 Usability

Simple and intuitive UI (Streamlit)

🔧 Maintainability

Modular code structure

Easy to update models or features

🚀 Key Features

📊 Academic Insight Dashboard

🧠 Feedback Sentiment Analysis

⚠️ Course Risk Detection

📈 Trend Analysis

🔍 Difficulty vs Satisfaction Mapping

📂 Dataset Upload & Auto Analysis

🏗 System Architecture
Student Feedback Data (CSV)
            │
            ▼
      Data Processing
      (Pandas / NumPy)
            │
            ▼
     Machine Learning Models
     (scikit-learn)
            │
            ▼
      Data Visualization
       (Matplotlib)
            │
            ▼
    Interactive Dashboard
        (Streamlit)
🛠 Tech Stack

Language

Python

Data Processing

Pandas

NumPy

Machine Learning

scikit-learn

Visualization

Matplotlib

Frontend / App

Streamlit

🚀 Deployment & Testing Plan
✅ Testing

Validate ML model predictions

Test edge cases (missing data, invalid inputs)

Verify dashboard outputs

🌐 Deployment

Deploy using Streamlit Cloud / Local server

Ensure app runs smoothly for external users

📊 Example Insights

Hardest courses

Courses with declining satisfaction

Most common student complaints

High-risk courses

🎯 Impact

EduMetrics enables:

Data-driven academic decisions

Early detection of course issues

Improved teaching strategies

Better student experience

🔮 Future Improvements

Real-time feedback system

Advanced NLP models

Instructor analytics

 setup-ds-environment
Multi-university benchmarking system

## ⚙️ Data Science Environment Setup

### 🖥️ System Information
- OS: Windows
- Python Version: 3.12.10
- Anaconda Version: 25.11.1

---

### 🐍 Python Verification
Command:
python --version

Output:
Python 3.12.10

---

### 📦 Conda Verification
Command:
conda --version

Output:
conda 25.11.1

---

### 🌱 Environment Setup
conda create -n ds_env python=3.10
conda activate ds_env

---

### ✅ Validation
python -c "print('Environment Ready')"

Output:
Environment Ready

Multi-college benchmarking
 main
