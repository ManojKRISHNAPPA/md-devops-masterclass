import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MicroDegree Registration",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "registered" not in st.session_state:
    st.session_state.registered = False

if "show_article" not in st.session_state:
    st.session_state.show_article = False

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.title {
    font-size: 3rem;
    font-weight: bold;
    color: #0072E3;
    text-align: center;
}
.tile {
    padding:20px;
    background-color:white;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    text-align:center;
}
.article-box {
    padding:25px;
    background-color:#ffffff;
    border-radius:15px;
    border:2px solid #0072E3;
    box-shadow:0px 6px 18px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="title">Welcome to MicroDegree 🚀</p>', unsafe_allow_html=True)

# ---------------- REGISTRATION ----------------
if not st.session_state.registered:

    with st.form("registration_form"):
        st.write("### 📝 Enter Your Details")
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        about = st.text_area("What are you excited to learn?", max_chars=200)

        submitted = st.form_submit_button("Register Now 🎉")

    if submitted:
        if not name or not email:
            st.error("Please fill required fields!")
        else:
            st.session_state.registered = True
            st.session_state.name = name
            st.session_state.email = email
            st.rerun()

# ---------------- AFTER LOGIN ----------------
if st.session_state.registered:

    st.success(f"🎊 Welcome {st.session_state.name}! You are registered.")

    st.markdown("---")

    # ---------------- VIDEOS ----------------
    st.markdown("## 🎥 Learn from These Videos")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.video("https://youtu.be/epRCCsUvJN8")

    with col2:
        st.video("https://youtu.be/m3YFGPoefeM")

    with col3:
        st.video("https://youtu.be/m7OiRsZ5nsk")

    with col4:
        st.markdown("[➡️ More Videos](https://www.youtube.com/@MicroDegree/videos)")

    st.markdown("---")

    # ---------------- ARTICLE TILE ----------------
    st.markdown("## 🚀 Explore New Articles")

    st.markdown("""
    <div class="tile">
    <h3>🤖 GenAI in CI/CD Pipeline</h3>
    <p>How AI is transforming DevOps automation.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Read Article 📖"):
        st.session_state.show_article = True

    # ---------------- ARTICLE ----------------
    if st.session_state.show_article:

        st.markdown('<div class="article-box">', unsafe_allow_html=True)

        st.markdown("## 🤖 How GenAI is Used in CI/CD Pipelines")

        st.markdown("""
### 🚀 Introduction
Generative AI is transforming CI/CD pipelines.

### 🔍 Intelligent Code Review
AI reviews pull requests and detects vulnerabilities.

### 🛡 Smart Security Scanning
Reads SAST reports and suggests fixes.

### 🤖 Pipeline Debugging
Summarizes logs and finds root causes.

### 📦 Docker Optimization
Suggests smaller base images.

### 🔄 GitOps Automation
Updates Helm and generates release notes.

### 🔮 Future Vision
✔ Self-healing pipelines  
✔ AI-generated Terraform  
✔ Auto rollback  
✔ Cost optimization  
""")

        if st.button("Close Article ❌"):
            st.session_state.show_article = False

        st.markdown('</div>', unsafe_allow_html=True)
