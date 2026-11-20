
import streamlit as st
from app.predict import predict_sms

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="SMS Shield | AI Spam Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #F5F7F6;
    color: #233B39;
}

.block-container {
    max-width: 1150px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.brand {
    color: #126B65;
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -1px;
}

.brand span {
    color: #F07862;
}

.nav-label {
    color: #647875;
    font-size: 14px;
    text-align: right;
    padding-top: 12px;
}

.hero {
    background: linear-gradient(120deg, #123F3C, #176B63);
    padding: 48px 45px;
    border-radius: 22px;
    color: white;
    margin-top: 22px;
    margin-bottom: 28px;
}

.hero-tag {
    color: #B9E5D9;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    color: white;
    font-size: 42px;
    line-height: 1.2;
    font-weight: 800;
    margin: 15px 0;
}

.hero p {
    color: #D6EAE5;
    font-size: 16px;
    max-width: 650px;
    line-height: 1.7;
}

.section-title {
    color: #183F3B;
    font-size: 23px;
    font-weight: 800;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #71817D;
    font-size: 14px;
    margin-bottom: 18px;
}

.panel {
    background: white;
    border: 1px solid #E5ECE9;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
}

.stat-card {
    background: white;
    border: 1px solid #E5ECE9;
    border-radius: 15px;
    padding: 20px;
    min-height: 115px;
}

.stat-label {
    color: #7B8985;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stat-value {
    color: #164E49;
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

.result-spam {
    background: #FFF0ED;
    border: 1px solid #F7C9C1;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    color: #B74738;
}

.result-ham {
    background: #E8F6EF;
    border: 1px solid #BDE5CF;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    color: #18734A;
}

.result-title {
    font-size: 25px;
    font-weight: 800;
    margin: 8px 0;
}

.result-description {
    font-size: 14px;
}

.footer {
    text-align: center;
    color: #82908C;
    font-size: 12px;
    padding-top: 25px;
    padding-bottom: 10px;
}

div.stButton > button {
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
    border: 1px solid #DCE7E3;
}

div.stButton > button[kind="primary"] {
    background: #176B63;
    color: white;
    border: none;
}

div.stButton > button[kind="primary"]:hover {
    background: #10544E;
    color: white;
}

textarea {
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "sms_input" not in st.session_state:
    st.session_state.sms_input = ""

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# ---------------- TOP NAVIGATION ----------------
nav1, nav2 = st.columns([3, 1])

with nav1:
    st.markdown(
        '<div class="brand">🛡️ SMS <span>SHIELD</span></div>',
        unsafe_allow_html=True
    )

with nav2:
    st.markdown(
        '<div class="nav-label">AI-Powered Message Security</div>',
        unsafe_allow_html=True
    )

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <div class="hero-tag">Intelligent NLP Security System</div>
    <h1>Detect Spam.<br>Stay One Step Ahead.</h1>
    <p>
        Analyse suspicious text messages using Machine Learning
        and Natural Language Processing. Identify unwanted messages
        and make smarter decisions before you respond.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- PROJECT STATISTICS ----------------
st.markdown('<div class="section-title">System Overview</div>',
            unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Inside the SMS Shield detection engine</div>',
            unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Dataset Messages</div>
        <div class="stat-value">5,572</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">ML Models Compared</div>
        <div class="stat-value">03</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Feature Extraction</div>
        <div class="stat-value">TF-IDF</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- MESSAGE ANALYSIS ----------------
st.markdown('<div class="section-title">Message Analysis</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Enter a message to check its classification.</div>',
    unsafe_allow_html=True
)

# Sample and clear buttons
st.markdown("**Quick test examples**")
b1, b2, b3 = st.columns([1, 1, 1])

with b1:
    if st.button("⚠️ Load spam example", use_container_width=True):
        st.session_state.sms_input = (
            "Congratulations! You have won a free cash prize. "
            "Call now to claim your reward!"
        )
        st.session_state.last_result = None

with b2:
    if st.button("✅ Load genuine example", use_container_width=True):
        st.session_state.sms_input = (
            "Hey, are we meeting for lunch today?"
        )
        st.session_state.last_result = None

with b3:
    if st.button("↻ Clear message", use_container_width=True):
        st.session_state.sms_input = ""
        st.session_state.last_result = None

st.markdown('<div class="panel">', unsafe_allow_html=True)

message = st.text_area(
    "SMS MESSAGE",
    key="sms_input",
    height=150,
    placeholder="Paste or type your SMS message here..."
)

analyze = st.button(
    "🔍  ANALYSE MESSAGE",
    type="primary",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if analyze:
    if not message.strip():
        st.warning("Please enter a message before starting the analysis.")
        st.session_state.last_result = None
    else:
        try:
            prediction, confidence = predict_sms(message)

            result_text = str(prediction).strip().lower()

            is_spam = (
                result_text in ["1", "true", "spam"]
                or (
                    "spam" in result_text
                    and "not spam" not in result_text
                    and "ham" not in result_text
                )
            )

            st.session_state.last_result = {
                "is_spam": is_spam,
                "confidence": confidence,
                "message": message
            }

        except Exception as error:
            st.error(f"Prediction error: {error}")
            st.session_state.last_result = None

# Display saved prediction
if st.session_state.last_result is not None:
    result = st.session_state.last_result

    st.write("")
    st.markdown("### Analysis Result")

    if result["is_spam"]:
        st.markdown("""
        <div class="result-spam">
            <div style="font-size:35px;">⚠️</div>
            <div class="result-title">SPAM MESSAGE DETECTED</div>
            <div class="result-description">
                This message has been classified as unwanted or potentially suspicious.
                Be cautious before clicking links or sharing personal information.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-ham">
            <div style="font-size:35px;">✓</div>
            <div class="result-title">GENUINE MESSAGE</div>
            <div class="result-description">
                This message has been classified as a normal message
                by the trained machine learning model.
            </div>
        </div>
        """, unsafe_allow_html=True)

    if result["confidence"] is not None:
        st.metric(
            "Model confidence",
            f"{float(result['confidence']) * 100:.2f}%"
        )
    else:
        st.info("A calibrated confidence score is not available for the selected model.")

    with st.expander("View analysed message"):
        st.write(result["message"])

# ---------------- HOW IT WORKS ----------------
st.write("")
st.divider()

st.markdown('<div class="section-title">How SMS Shield Works</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">A machine learning pipeline that processes and classifies text.</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="panel">
        <h3 style="color:#176B63;">01 · Preprocessing</h3>
        <p style="color:#71817D;">
        Converts text to lowercase, removes unwanted characters,
        eliminates stopwords and applies stemming.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="panel">
        <h3 style="color:#176B63;">02 · TF-IDF</h3>
        <p style="color:#71817D;">
        Converts cleaned messages into numerical features
        that the machine learning model can understand.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="panel">
        <h3 style="color:#176B63;">03 · Prediction</h3>
        <p style="color:#71817D;">
        The trained classifier analyses the message and
        predicts whether it is spam or genuine.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <b>SMS SHIELD</b> · NLP & Machine Learning Project<br>
    Built with Python · Scikit-learn · TF-IDF · Streamlit
</div>
""", unsafe_allow_html=True)
