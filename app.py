import streamlit as st

# =====================================

# PAGE CONFIG

# =====================================

st.set_page_config(
page_title="Credit Risk Intelligence Platform",
page_icon="🏦",
layout="wide",
initial_sidebar_state="expanded"
)

# =====================================

# CUSTOM CSS

# =====================================

st.markdown("""

<style>

/* Main Background */
.stApp {
    background-color: #0F172A;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #334155;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 20px;
}

/* Section Title */
.section-title {
    font-size: 2rem;
    font-weight: 700;
    color: white;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Metric Cards */
.metric-card {
    background: linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.metric-card h3 {
    color: white;
    margin: 0;
}

.metric-card h1 {
    color: white;
    margin-top: 10px;
}

/* Content Card */
.card {
    background-color: #1E293B;
    padding: 25px;
    border-radius: 15px;
    color: white;
    border: 1px solid #334155;
    margin-top: 20px;
}

/* Risk Badges */
.low-risk {
    color: #22C55E;
    font-size: 24px;
    font-weight: bold;
}

.medium-risk {
    color: #F59E0B;
    font-size: 24px;
    font-weight: bold;
}

.high-risk {
    color: #EF4444;
    font-size: 24px;
    font-weight: bold;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #2563EB;
    color: white;
    font-weight: bold;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

/* Text Input */
.stTextInput > div > div > input {
    border-radius: 10px;
}

</style>

""", unsafe_allow_html=True)

# =====================================

# TITLE

# =====================================

st.markdown("""

<div class="main-title">
🏦 Credit Risk Intelligence Platform
</div>
""", unsafe_allow_html=True)

# =====================================

# SIDEBAR

# =====================================

st.sidebar.title("📊 Navigation")

st.sidebar.markdown("---")

st.sidebar.info(
"""
### Model Information

**Model:** LightGBM

**ROC-AUC:** 0.767

**Dataset:** Home Credit

**Records:** 307K+
"""
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📈 Risk Prediction",
        "🔍 Explainability",
        "💬 Talk To Data"
    ],
    label_visibility="collapsed"
)
# =====================================

# HOME PAGE

# =====================================
st.success(
    "Welcome to the Credit Risk Intelligence Platform. Explore risk prediction, explainability, and AI-powered analytics."
)
if page == "🏠 Home":


    st.markdown(
        '<div class="section-title">Dashboard Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>ROC-AUC</h3>
            <h1>0.767</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Records</h3>
            <h1>307K+</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Features</h3>
            <h1>250</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Defaults</h3>
            <h1>24.8K</h1>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="metric-card">
            <h3>Chatbot</h3>
            <h1>AI</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>🏦 Project Overview</h3>

        <ul>
            <li>Predict customer default risk</li>
            <li>Generate explainable risk scores</li>
            <li>Analyze model decisions using SHAP</li>
            <li>Query data using natural language</li>
            <li>Support banking lending decisions</li>
        </ul>

        <h3>🚀 Key Features</h3>

        <ul>
            <li>Credit Risk Prediction</li>
            <li>Risk Scoring Engine</li>
            <li>Recommendation Engine</li>
            <li>SHAP Explainability</li>
            <li>Natural Language to SQL Chatbot</li>
        </ul>
                
        <h3>🛠 Technology Stack</h3>

        <ul>
            <li>Frontend: Streamlit</li>
            <li>Machine Learning: LightGBM</li>
            <li>Explainability: SHAP</li>
            <li>AI Assistant: Groq Llama 3.3</li>
            <li>Database: SQLite</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# =====================================

# RISK PREDICTION PAGE

# =====================================

elif page == "📈 Risk Prediction":


    st.markdown(
        '<div class="section-title">Credit Risk Prediction</div>',
        unsafe_allow_html=True
    )

    probability = st.slider(
        "Default Probability",
        0.0,
        1.0,
        0.50
    )

    from src.ml.risk_logic import (
        risk_score,
        risk_band,
        recommendation
    )

    score = risk_score(probability)
    band = risk_band(score)
    advice = recommendation(score)

    st.markdown(f"""
    <div class="metric-card">
        <h3>Risk Score</h3>
        <h1>{score}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if band == "Low Risk":
        st.markdown(
            f'<p class="low-risk">✅ {band}</p>',
            unsafe_allow_html=True
        )

    elif band == "Medium Risk":
        st.markdown(
            f'<p class="medium-risk">⚠️ {band}</p>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<p class="high-risk">🚨 {band}</p>',
            unsafe_allow_html=True
        )

    st.info(
        f"Recommendation: {advice}"
    )


# =====================================

# EXPLAINABILITY PAGE

# =====================================

elif page == "🔍 Explainability":


    st.markdown(
        '<div class="section-title">Model Explainability</div>',
        unsafe_allow_html=True
    )

    st.image(
        "documents/shap_summary.png",
        caption="SHAP Summary Plot",
        use_container_width=True
    )

    st.image(
        "documents/shap_bar.png",
        caption="SHAP Feature Importance",
        use_container_width=True
    )

# =====================================

# TALK TO DATA PAGE

# =====================================

elif page == "💬 Talk To Data":


    st.markdown(
        '<div class="section-title">AI Banking Assistant</div>',
        unsafe_allow_html=True
    )

    question = st.text_input(
        "Ask a business question"
    )

    if st.button("Ask AI"):

        import sys
        sys.path.append("src/chatbot")

        from chatbot import ask

        with st.spinner("Analyzing data..."):
            answer = ask(question)

        st.markdown("""
        ### 🤖 Assistant Response
        """)

        st.info(answer)

st.markdown("---")

st.caption(
    "🏦 Credit Risk Intelligence Platform | LightGBM • SHAP • Groq • Streamlit"
)