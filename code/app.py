import streamlit as st
import os
from database import create_users_table, register_user, authenticate_user, get_user_by_email

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MicroDegree Platform",
    layout="wide"
)

# ---------------- INITIALIZE DATABASE ----------------
# Create users table if it doesn't exist
if os.getenv('DB_PASSWORD'):
    create_users_table()

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None

if "user_data" not in st.session_state:
    st.session_state.user_data = None

if "show_article" not in st.session_state:
    st.session_state.show_article = False

if "page" not in st.session_state:
    st.session_state.page = "login"

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
.profile-card {
    padding:30px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius:15px;
    box-shadow:0px 6px 18px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HELPER FUNCTIONS ----------------
def logout():
    """Clear session state and logout user."""
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.session_state.user_data = None
    st.session_state.page = "login"
    st.session_state.show_article = False
    st.rerun()

# ---------------- TITLE ----------------
st.markdown('<p class="title">Welcome to MicroDegree 🚀</p>', unsafe_allow_html=True)

# ---------------- LOGGED OUT VIEW ----------------
if not st.session_state.logged_in:

    # Check if DB_PASSWORD is set
    if not os.getenv('DB_PASSWORD'):
        st.error("⚠️ Database is not configured. Please set the DB_PASSWORD environment variable.")
        st.stop()

    # Create tabs for Login and Register
    tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])

    # ---------------- LOGIN TAB ----------------
    with tab1:
        st.markdown("### Login to Your Account")

        with st.form("login_form"):
            login_email = st.text_input("Email Address", key="login_email")
            login_password = st.text_input("Password", type="password", key="login_password")
            login_submitted = st.form_submit_button("Login 🚀")

        if login_submitted:
            if not login_email or not login_password:
                st.error("Please enter both email and password!")
            else:
                with st.spinner("Authenticating..."):
                    user_data = authenticate_user(login_email, login_password)

                    if user_data:
                        st.session_state.logged_in = True
                        st.session_state.user_email = login_email
                        st.session_state.user_data = user_data
                        st.success(f"Welcome back, {user_data['full_name']}! 🎉")
                        st.rerun()
                    else:
                        st.error("Invalid email or password. Please try again.")

    # ---------------- REGISTER TAB ----------------
    with tab2:
        st.markdown("### Create Your Account")

        with st.form("registration_form"):
            reg_name = st.text_input("Full Name *", key="reg_name")
            reg_email = st.text_input("Email Address *", key="reg_email")
            reg_password = st.text_input("Password *", type="password", key="reg_password")
            reg_password_confirm = st.text_input("Confirm Password *", type="password", key="reg_password_confirm")
            reg_phone = st.text_input("Phone Number (Optional)", key="reg_phone")

            reg_submitted = st.form_submit_button("Register Now 🎉")

        if reg_submitted:
            # Validation
            if not reg_name or not reg_email or not reg_password:
                st.error("Please fill all required fields (marked with *)!")
            elif reg_password != reg_password_confirm:
                st.error("Passwords do not match!")
            elif len(reg_password) < 6:
                st.error("Password must be at least 6 characters long!")
            else:
                with st.spinner("Creating your account..."):
                    success, message = register_user(
                        email=reg_email,
                        password=reg_password,
                        full_name=reg_name,
                        phone_number=reg_phone if reg_phone else None
                    )

                    if success:
                        st.success("🎊 Registration successful! Please login with your credentials.")
                    else:
                        st.error(f"Registration failed: {message}")

# ---------------- LOGGED IN VIEW ----------------
else:
    # Get fresh user data
    if not st.session_state.user_data:
        st.session_state.user_data = get_user_by_email(st.session_state.user_email)

    user = st.session_state.user_data

    # ---------------- TOP BAR WITH LOGOUT ----------------
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("Logout 🚪", type="primary"):
            logout()

    st.markdown("---")

    # ---------------- PROFILE CARD ----------------
    st.markdown("## 👤 Your Profile")

    st.markdown(f"""
    <div class="profile-card">
        <h2>Hello, {user['full_name']}! 👋</h2>
        <p><strong>📧 Email:</strong> {user['email']}</p>
        <p><strong>📱 Phone:</strong> {user['phone_number'] if user.get('phone_number') else 'Not provided'}</p>
        <p><strong>📅 Member Since:</strong> {user['created_at'].strftime('%B %d, %Y') if user.get('created_at') else 'N/A'}</p>
    </div>
    """, unsafe_allow_html=True)

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
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
