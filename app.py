import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import json
import os
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="EduMetrics - Data-Driven Academic Analytics", page_icon="📊", layout="wide")

# Custom CSS for modern UI and Animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Fade-in Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stApp {
        animation: fadeIn 0.8s ease-out;
    }

    /* Card Hover Effects */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid #eee;
    }
    
    .metric-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        border-color: #ff4b4b;
    }

    /* Button Animations */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3.5em;
        background: linear-gradient(45deg, #ff4b4b, #ff7675);
        color: white;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
    }

    /* Pulse Animation for important elements */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-element {
        animation: pulse 2s infinite;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #eee;
    }

    /* Header styling */
    .header-style {
        color: #1e3d59;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATABASE FOR AUTH ---
USER_DB_FILE = "users.json"

def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f)

# --- ANALYSIS LOGIC ---
def perform_sentiment_analysis(df):
    # Simple ML pipeline for sentiment (Mock training if no model exists)
    # In a real app, this would be pre-trained
    texts = [
        "Great course!", "Excellent teaching.", "Loved the labs.",
        "Terrible experience.", "Very difficult and confusing.", "Waste of time.",
        "Good but can be improved.", "Average course.", "It was okay."
    ]
    labels = ["Positive", "Positive", "Positive", "Negative", "Negative", "Negative", "Neutral", "Neutral", "Neutral"]
    
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])
    pipeline.fit(texts, labels)
    
    df['sentiment'] = pipeline.predict(df['feedback'])
    return df

def calculate_course_health(df):
    # Course Health Score = (Teaching Quality * 0.4 + Satisfaction * 0.4 + (6 - Difficulty) * 0.2) / 5 * 100
    df['health_score'] = (df['teaching_quality'] * 0.4 + df['satisfaction'] * 0.4 + (6 - df['difficulty']) * 0.2) / 5 * 100
    return df

def predict_risk(df):
    # Logic: If health score < 50 or difficulty > 4 and satisfaction < 2
    def risk_logic(row):
        if row['health_score'] < 50 or (row['difficulty'] >= 4 and row['satisfaction'] <= 2):
            return "High Risk"
        elif row['health_score'] < 70:
            return "Moderate Risk"
        else:
            return "Low Risk"
    
    df['risk_level'] = df.apply(risk_logic, axis=1)
    return df

def get_recommendations(row):
    if row['risk_level'] == "High Risk":
        return "⚠️ Immediate review of course load and teaching methods required. Consider student-faculty meeting."
    elif row['risk_level'] == "Moderate Risk":
        return "💡 Minor adjustments in assignment load or lab clarity suggested."
    else:
        return "✅ Course is performing well. Maintain current teaching standards."

# --- UI COMPONENTS ---
def login_signup():
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://img.icons8.com/clouds/200/000000/education.png" width="150">
        </div>
    """, unsafe_allow_html=True)
    st.title("📊 EduMetrics")
    st.subheader("Data-Driven Academic Feedback Analytics")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    users = load_users()
    
    with tab1:
        st.markdown("### Welcome Back!")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"Logged in as {username}")
                st.balloons()
                st.rerun()
            else:
                st.error("Invalid username or password")
                
    with tab2:
        st.markdown("### Create an Account")
        new_user = st.text_input("Choose Username", key="reg_user")
        new_pass = st.text_input("Choose Password", type="password", key="reg_pass")
        confirm_pass = st.text_input("Confirm Password", type="password", key="reg_confirm")
        if st.button("Sign Up"):
            if new_user in users:
                st.warning("Username already exists")
            elif new_pass != confirm_pass:
                st.error("Passwords do not match")
            elif new_user and new_pass:
                users[new_user] = new_pass
                save_users(users)
                st.success("Account created successfully! Please login.")
            else:
                st.error("Please fill all fields")

def main_dashboard():
    st.sidebar.image("https://img.icons8.com/clouds/200/000000/combo-chart.png", width=100)
    st.sidebar.title(f"Welcome, {st.session_state['username']}!")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
    
    st.sidebar.markdown("---")
    uploaded_file = st.sidebar.file_uploader("Upload Student Feedback (CSV)", type="csv")

    # --- SAMPLE FILES INFO ---
    with st.sidebar.expander("📁 Sample Input Files"):
        st.write("Find these mixed-feedback batches in `data/`:")
        st.code("feedback_batch_1.csv")
        st.code("feedback_batch_2.csv")
        st.code("feedback_batch_3.csv")
        st.code("feedback_batch_4.csv")
    
    if uploaded_file is not None:
        with st.status("🔍 Analyzing Student Feedback Data...", expanded=True) as status:
            st.write("Reading CSV...")
            df = pd.read_csv(uploaded_file)
            
            st.write("Running Sentiment Analysis...")
            df = perform_sentiment_analysis(df)
            
            st.write("Calculating Course Health Scores...")
            df = calculate_course_health(df)
            
            st.write("Predicting Academic Risks...")
            df = predict_risk(df)
            
            status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
        
        st.snow()
        st.title("📈 Academic Insights Dashboard")
        st.markdown(f"**Analyzing feedback from {len(df)} student responses.**")
        
        # --- KEY METRICS ---
        st.markdown("### Key Performance Indicators")
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        
        with m_col1:
            avg_health = df['health_score'].mean()
            st.markdown(f"""
                <div class="metric-card">
                    <p style='color:#636e72; font-size:14px; margin-bottom:5px;'>Avg Health Score</p>
                    <h2 style='color:#ff4b4b; margin:0;'>{avg_health:.1f}%</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with m_col2:
            positive_perc = (df['sentiment'] == "Positive").mean() * 100
            st.markdown(f"""
                <div class="metric-card">
                    <p style='color:#636e72; font-size:14px; margin-bottom:5px;'>Positive Sentiment</p>
                    <h2 style='color:#00b894; margin:0;'>{positive_perc:.1f}%</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with m_col3:
            high_risk_count = (df['risk_level'] == "High Risk").sum()
            st.markdown(f"""
                <div class="metric-card">
                    <p style='color:#636e72; font-size:14px; margin-bottom:5px;'>High Risk Courses</p>
                    <h2 style='color:#d63031; margin:0;'>{high_risk_count}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with m_col4:
            total_feedback = len(df)
            st.markdown(f"""
                <div class="metric-card">
                    <p style='color:#636e72; font-size:14px; margin-bottom:5px;'>Total Feedbacks</p>
                    <h2 style='color:#0984e3; margin:0;'>{total_feedback}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- VISUALIZATIONS ---
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("Sentiment Distribution")
            fig, ax = plt.subplots(figsize=(8, 5))
            # Enhanced visual styling
            sns.set_style("whitegrid")
            sns.countplot(data=df, x='sentiment', palette='viridis', ax=ax, order=['Positive', 'Neutral', 'Negative'])
            ax.set_title("Distribution of Student Sentiments", fontsize=14, pad=20)
            ax.set_xlabel("Sentiment Category", fontsize=12)
            ax.set_ylabel("Count of Feedbacks", fontsize=12)
            plt.tight_layout()
            st.pyplot(fig)
            
        with c2:
            st.subheader("Course Health vs Difficulty")
            fig, ax = plt.subplots(figsize=(8, 5))
            # Enhanced scatter plot visibility
            sns.set_style("whitegrid")
            scatter = sns.scatterplot(
                data=df, 
                x='difficulty', 
                y='health_score', 
                hue='risk_level', 
                size='satisfaction', 
                sizes=(100, 400), 
                palette={'Low Risk': '#00b894', 'Moderate Risk': '#f1c40f', 'High Risk': '#d63031'},
                alpha=0.8,
                edgecolor='black',
                ax=ax
            )
            ax.set_title("Health Score vs. Course Difficulty", fontsize=14, pad=20)
            ax.set_xlabel("Difficulty Level (1-5)", fontsize=12)
            ax.set_ylabel("Health Score (%)", fontsize=12)
            ax.legend(title="Risk Level & Satisfaction", bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            st.pyplot(fig)
            
        st.markdown("---")
        
        # --- COURSE ANALYSIS TABLE ---
        st.subheader("Detailed Course Performance & Recommendations")
        
        display_df = df[['course_name', 'sentiment', 'health_score', 'risk_level']]
        display_df['Recommendation'] = df.apply(get_recommendations, axis=1)
        
        st.dataframe(display_df.style.background_gradient(subset=['health_score'], cmap='RdYlGn'))
        
        # --- DOWNLOAD PROCESSED DATA ---
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Processed Analysis CSV",
            data=csv,
            file_name='edumetrics_analysis.csv',
            mime='text/csv',
        )
        
    else:
        st.info("👋 Please upload a CSV file to begin the analysis.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
                <div class="metric-card">
                    <img src="https://img.icons8.com/clouds/100/000000/upload.png" width="100">
                    <p><b>1. Upload CSV</b></p>
                    <p style='font-size: 12px;'>Drag and drop your student feedback data.</p>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                <div class="metric-card">
                    <img src="https://img.icons8.com/clouds/100/000000/brainstorming.png" width="100">
                    <p><b>2. AI Processing</b></p>
                    <p style='font-size: 12px;'>Sentiment analysis and risk prediction.</p>
                </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
                <div class="metric-card">
                    <img src="https://img.icons8.com/clouds/100/000000/presentation.png" width="100">
                    <p><b>3. Insights Dashboard</b></p>
                    <p style='font-size: 12px;'>Visual trends and recommendations.</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Show sample data format
        st.markdown("#### Expected CSV Format:")
        sample_format = pd.DataFrame({
            'course_name': ['Math', 'Physics'],
            'teaching_quality': [5, 2],
            'difficulty': [3, 5],
            'satisfaction': [4, 1],
            'assignment_load': [2, 5],
            'feedback': ['Great teacher!', 'Too hard and confusing.']
        })
        st.table(sample_format)

# --- APP ENTRY POINT ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login_signup()
else:
    main_dashboard()

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: grey; font-size: small;">
        © 2026 EduMetrics Platform | Powered by Python, Pandas & Streamlit | 🚀 Developed for Academic Excellence
    </div>
""", unsafe_allow_html=True)
