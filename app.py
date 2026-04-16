import streamlit as st
import joblib
import tldextract
from urllib.parse import urlparse

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️",
    layout="wide"
)

# ===============================
# CUSTOM UI STYLE
# ===============================
st.markdown("""
<style>

.metric-box{
padding:20px;
border-radius:10px;
color:white;
text-align:center;
font-weight:bold;
font-size:18px;
}

.red-box{
background:#e74c3c;
}

.green-box{
background:#27ae60;
}

.purple-box{
background:#6c5ce7;
}

.risk-bar{
height:15px;
border-radius:10px;
background:linear-gradient(to right, red, orange, yellow, green);
margin-top:10px;
margin-bottom:10px;
}

.result-safe{
background:#27ae60;
padding:15px;
border-radius:8px;
text-align:center;
font-weight:bold;
font-size:18px;
color:white;
}

.result-danger{
background:#e74c3c;
padding:15px;
border-radius:8px;
text-align:center;
font-weight:bold;
font-size:18px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# LOAD MODEL
# ===============================
model = joblib.load("automl_model.pkl")

# ===============================
# HEADER
# ===============================
st.title("🛡️ CyberShield AI")
st.caption("AI-Powered Phishing Website Detection System")

st.divider()

# ===============================
# SIDEBAR
# ===============================
st.sidebar.header("Security Scanner")

st.sidebar.write("""
CyberShield analyzes website URLs using
machine learning (AUTO ML).

Detection signals:

• HTTPS security  
• URL length anomalies  
• Subdomain manipulation  
• Suspicious characters  
• Domain spoofing
""")

st.sidebar.divider()
st.sidebar.success("Model: AutoML Classifier")

# ===============================
# FEATURE EXTRACTION
# ===============================
def extract_features(url):

    parsed = urlparse(url)

    # SSL
    ssl = 1 if parsed.scheme == "https" else -1

    # URL Length
    if len(url) < 54:
        url_len = 1
    elif len(url) <= 75:
        url_len = 0
    else:
        url_len = -1

    # Subdomain
    sub = tldextract.extract(url).subdomain

    if sub == "":
        subdomain = 1
    elif sub.count(".") == 1:
        subdomain = 0
    else:
        subdomain = -1

    # Prefix-Suffix
    prefix = -1 if "-" in parsed.netloc else 1

    # @ symbol
    at_symbol = -1 if "@" in url else 1

    features = [ssl, url_len, subdomain, prefix, at_symbol]

    indicators = {
        "HTTPS Enabled": ssl,
        "URL Length Status": url_len,
        "Subdomain Pattern": subdomain,
        "Domain Hyphen Check": prefix,
        "At Symbol Check": at_symbol
    }

    return features, indicators

# ===============================
# URL INPUT
# ===============================
st.subheader("🔎 Website Security Scan")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

st.divider()

# ===============================
# SCAN BUTTON
# ===============================
if st.button("Run Security Scan", use_container_width=True):

    if url == "":
        st.warning("Please enter a URL")

    else:

        features, indicators = extract_features(url)

        prediction = model.predict([features])
        probability = model.predict_proba([features])

        phishing_risk = probability[0][1] * 100
        legit_score = probability[0][0] * 100
        confidence = max(phishing_risk, legit_score)

        st.subheader("Threat Analysis")

        col1, col2, col3 = st.columns(3)

        # Phishing Risk
        with col1:
            st.markdown(f"""
            <div class="metric-box red-box">
            Phishing Risk<br>
            {phishing_risk:.2f}%
            </div>
            """, unsafe_allow_html=True)

        # Legitimate Score
        with col2:
            st.markdown(f"""
            <div class="metric-box green-box">
            Legitimate Score<br>
            {legit_score:.2f}%
            </div>
            """, unsafe_allow_html=True)

        # Model Confidence
        with col3:
            st.markdown(f"""
            <div class="metric-box purple-box">
            Model Confidence<br>
            {confidence:.2f}%
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # ===============================
        # RISK BAR
        # ===============================
        st.subheader("Risk Level")

        st.markdown('<div class="risk-bar"></div>', unsafe_allow_html=True)

        if prediction[0] == 0:
            st.markdown("""
            <div class="result-safe">
            Risk Level: Website appears LEGITIMATE!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-danger">
            Risk Level: Potential PHISHING detected
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # ===============================
        # SECURITY INDICATORS
        # ===============================
        st.subheader("Security Indicators")

        col1, col2 = st.columns(2)

        with col1:

            if indicators["HTTPS Enabled"] == 1:
                st.success("HTTPS encryption detected")
            else:
                st.error("No HTTPS encryption")

            if indicators["Domain Hyphen Check"] == 1:
                st.success("Domain structure looks normal")
            else:
                st.warning("Suspicious '-' detected in domain")

        with col2:

            if indicators["Subdomain Pattern"] == 1:
                st.success("Subdomain structure normal")
            else:
                st.warning("Suspicious subdomain pattern")

            if indicators["At Symbol Check"] == 1:
                st.success("No '@' symbol detected")
            else:
                st.error("URL contains '@' symbol")

        st.divider()

        st.subheader("Extracted Feature Values")
        st.write(indicators)

# ===============================
# FOOTER
# ===============================
st.divider()


st.markdown(
"""
<center>

Developed by **Parjinder Singh**  
AI • Machine Learning • Cybersecurity

<br><br>

<a href='https://www.linkedin.com/in/parjinder-singh' target='_blank' style='
background-color:#0e76a8;
color:white;
padding:8px 16px;
text-decoration:none;
border-radius:5px;
display:inline-block;
font-weight:bold;'>
🔗 Connect on LinkedIn
</a>

</center>
""",
unsafe_allow_html=True
)