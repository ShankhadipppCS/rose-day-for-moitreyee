import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Happy Rose Day ❤️",
    page_icon="🌹",
    layout="centered"
)

# ---------------- BEAUTIFUL ROSE THEME CSS ----------------
st.markdown("""
<style>

/* Full background */
.stApp {
    background: linear-gradient(135deg, #ffd6e0, #fff0f5, #ffe5ec);
    background-attachment: fixed;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Card container */
.card {
    background: rgba(255, 255, 255, 0.75);
    border-radius: 22px;
    padding: 30px;
    box-shadow: 0 15px 35px rgba(201, 24, 74, 0.25);
    margin-top: 40px;
}

/* Text styles */
.title {
    font-size: 42px;
    font-weight: 800;
    color: #c9184a;
    text-align: center;
}

.subtitle {
    font-size: 24px;
    color: #800f2f;
    text-align: center;
    margin-top: 10px;
}

.message {
    font-size: 20px;
    color: #590d22;
    text-align: center;
    line-height: 1.7;
    margin-top: 18px;
}

/* Heart animation */
.heart {
    font-size: 34px;
    text-align: center;
    margin-top: 20px;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

/* Center button */
.stButton > button {
    background-color: #c9184a;
    color: white;
    font-size: 18px;
    padding: 10px 30px;
    border-radius: 30px;
    border: none;
    display: block;
    margin: 25px auto 0 auto;
}

.stButton > button:hover {
    background-color: #a4133c;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.markdown("""
    <div class="card">
        <div class="title">Hey You 🌸</div>
        <div class="subtitle">Someone has something special for you…</div>
        <div class="heart">💗 💗 💗</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Take the first step 🌱"):
        st.session_state.step = 2

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.markdown("""
    <div class="card">
        <div class="title">A Little Closer 💕</div>
        <div class="message">
            Every rose has a story…<br>
            and this one blooms just for you.
        </div>
        <div class="heart">🌹</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Reveal more 🌸"):
        st.session_state.step = 3

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.markdown("""
    <div class="card">
        <div class="title">Why You Matter 🌹</div>
        <div class="message">
            You make ordinary moments beautiful,<br>
            smiles effortless,<br>
            and hearts feel at home.<br><br>
            Just being you is enough.
        </div>
        <div class="heart">💖</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Final Surprise 💝"):
        st.session_state.step = 4

# ---------------- FINAL STEP ----------------
elif st.session_state.step == 4:
    st.balloons()
    st.markdown("""
    <div class="card">
        <div class="title">Happy Rose Day 🌹</div>
        <div class="subtitle">Moitreyee ❤️</div>
        <div class="message">
            This rose may be virtual,<br>
            but the feelings behind it are very real.<br><br>
            Thank you for being the most beautiful part<br>
            of my everyday world.
        </div>
        <div class="heart">🌹 🌹 🌹</div>
    </div>
    """, unsafe_allow_html=True)

