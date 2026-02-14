import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MicroDegree Registration",
    layout="wide",
    initial_sidebar_state="auto"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
        .main {
            background-color: #F5F5F5;
        }
        .title {
            font-size: 3rem;
            font-weight: bold;
            color: #0072E3;
            text-align: center;
        }
        .sub-title {
            font-size: 1.4rem;
            color: #333;
            text-align: center;
        }
        .tile {
            padding:20px;
            background-color:white;
            border-radius:15px;
            box-shadow:0px 4px 12px rgba(0,0,0,0.1);
            text-align:center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown('<p class="title">Welcome to MicroDegree 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Register below to unlock exciting projects & tutorials!</p>', unsafe_allow_html=True)

# ---------------- REGISTRATION FORM ----------------
with st.form("registration_form", clear_on_submit=False):
    st.write("### 📝 Enter Your Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    about = st.text_area("What are you excited to learn?", max_chars=200)

    submitted = st.form_submit_button("Register Now 🎉")

# ---------------- AFTER SUBMIT ----------------
if submitted:
    if not name or not email:
        st.error("Please fill in all required fields!")
    else:
        st.balloons()
        st.success(
            f"🎊 **Welcome {name}!** You’re now registered with **{email}**.\n\n"
            f"📣 Fantastic! You just unlocked amazing projects!"
        )

        # Unlocked Projects
        st.markdown(
            """
            <div style="padding:15px; background-color:#fff; border-radius:10px; border:2px solid #0072E3;">
            <h3 style="color:#0072E3;">🔥 You Unlocked:</h3>
            <ul style="font-size:1.1rem;">
                <li>📌 Python Full Stack Micro Projects</li>
                <li>📌 AI & ML Hands-On Mini Projects</li>
                <li>📌 Web3 & Blockchain Beginners Pack</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        # ---------------- VIDEO SECTION ----------------
        st.markdown('<h2 style="text-align:center; color:#0072E3;">🎥 Learn from These Videos!</h2>', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown('<p class="sub-title">MicroDegree Intro</p>', unsafe_allow_html=True)
            st.video("https://youtu.be/epRCCsUvJN8")

        with col2:
            st.markdown('<p class="sub-title">Project Ideas Explained</p>', unsafe_allow_html=True)
            st.video("https://youtu.be/m3YFGPoefeM")

        with col3:
            st.markdown('<p class="sub-title">Prompt Engineering</p>', unsafe_allow_html=True)
            st.video("https://youtu.be/m7OiRsZ5nsk")

        with col4:
            st.markdown('<p class="sub-title">More from MicroDegree Channel</p>', unsafe_allow_html=True)
            st.markdown("[➡️ Click to view videos](https://www.youtube.com/@MicroDegree/videos)")

        st.markdown("---")

        # ---------------- GENAI ARTICLE TILE ----------------
        st.markdown('<h2 style="text-align:center; color:#0072E3;">🚀 Explore New Articles</h2>', unsafe_allow_html=True)

        if "show_article" not in st.session_state:
            st.session_state.show_article = True  # Auto popup first time

        colA, colB = st.columns(2)

        with colA:
            st.markdown(
                """
                <div class="tile">
                <h3 style="color:#0072E3;">🤖 GenAI in CI/CD Pipeline</h3>
                <p>How AI is transforming DevOps automation & pipelines.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button("Read Article 📖"):
                st.session_state.show_article = True

        # ---------------- MODAL POPUP ----------------
        if st.session_state.show_article:
            with st.modal("🤖 How GenAI is Used in CI/CD Pipelines"):
                st.markdown("""
                ## 🚀 Introduction
                Generative AI is transforming modern DevOps pipelines by adding intelligence to automation.

                ---
                ## 🔍 1️⃣ Intelligent Code Review
                - AI reviews Pull Requests
                - Detects vulnerabilities
                - Suggests optimized code
                - Prevents insecure merges

                ---
                ## 🛡 2️⃣ Smart Security Scanning
                - Reads SAST/DAST reports
                - Explains vulnerabilities clearly
                - Suggests fixes automatically
                - Reduces debugging time

                ---
                ## 🤖 3️⃣ Pipeline Failure Debugging
                - AI summarizes CI/CD logs
                - Identifies root cause
                - Suggests next steps instantly

                ---
                ## 📦 4️⃣ Docker & Kubernetes Optimization
                - Suggests minimal base images
                - Optimizes Docker layers
                - Recommends HPA tuning

                ---
                ## 🔄 5️⃣ GitOps + AI Automation
                - Auto updates Helm values
                - Generates release notes
                - Suggests version upgrades

                ---
                ## 🔮 Future Vision
                ✔ Self-healing pipelines  
                ✔ Auto rollback via anomaly detection  
                ✔ AI-generated Terraform modules  
                ✔ Intelligent cost optimization  

                ---
                ### ✨ DevOps is evolving from Automation → Intelligence
                """)

                if st.button("Close ❌"):
                    st.session_state.show_article = False

        st.markdown("---")
        st.markdown('<h3 style="text-align:center;">✨ Keep Learning & Build Cool Stuff!</h3>', unsafe_allow_html=True)
