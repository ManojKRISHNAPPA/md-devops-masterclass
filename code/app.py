import streamlit as st

# Page config for responsive layout
st.set_page_config(
    page_title="MicroDegree Registration",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- CSS for Styling ---
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
            font-size: 1.6rem;
            color: #333;
            text-align: center;
        }
        .highlight {
            color: #E63946;
            font-weight: bold;
        }
        .video-container {
            margin-top: 15px;
            margin-bottom: 15px;
        }
    </style>
    """, unsafe_allow_html=True
)

# --- Title ---
st.markdown('<p class="title">Welcome to MicroDegree 🚀</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Register below to unlock exciting projects & tutorials!</p>', unsafe_allow_html=True)

# --- Registration Form ---
with st.form("registration_form", clear_on_submit=False):
    st.write("### 📝 Enter Your Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    about = st.text_area("What are you excited to learn?", max_chars=200)
    
    submitted = st.form_submit_button("Register Now 🎉")

if submitted:
    # Validation
    if not name or not email:
        st.error("Please fill in all required fields!")
    else:
        # Success
        st.balloons()
        st.success(
            f"🎊 **Welcome {name}!** You’re now registered with **{email}**.\n\n"
            f"📣 *Fantastic! You just unlocked amazing projects!*"
        )

        # Display unlocked project messages
        st.markdown(
            """
            <div style="padding:15px; background-color:#fff; border-radius:10px; border:2px solid #0072E3;">
            <h3 style="color:#0072E3;">🔥 You Unlocked:</h3>
            <ul style="font-size:1.2rem;">
                <li>📌 Python Full Stack Micro Projects</li>
                <li>📌 AI & ML Hands-On Mini Projects</li>
                <li>📌 Web3 & Blockchain Beginners Pack</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")
        
        # Video Section
        st.markdown('<h2 style="text-align:center; color:#0072E3;">🎥 Learn from These Videos!</h2>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown('<p class="sub-title">MicroDegree Intro</p>', unsafe_allow_html=True)
            st.video("https://youtu.be/epRCCsUvJN8")
        
        with col2:
            st.markdown('<p class="sub-title">Project Ideas Explained</p>', unsafe_allow_html=True)
            st.video("https://youtu.be/m3YFGPoefeM")

        with col3:
            st.markdown('<p class="sub-title">More from MicroDegree Channel</p>', unsafe_allow_html=True)
            st.markdown("[➡️ Click to view videos](https://www.youtube.com/@MicroDegree/videos)")

        st.markdown("---")
        st.markdown('<h3 style="text-align:center;">✨ Keep Learning & Build Cool Stuff!</h3>', unsafe_allow_html=True)
