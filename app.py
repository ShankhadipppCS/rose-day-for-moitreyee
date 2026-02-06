import streamlit as st
import time

st.set_page_config(
    page_title="Happy Rose Day ❤️",
    page_icon="🌹",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffd1dc, #fff0f5);
}
.title {
    font-size: 42px;
    font-weight: bold;
    color: #c9184a;
    text-align: center;
}
.subtitle {
    font-size: 22px;
    color: #6a040f;
    text-align: center;
}
.message {
    font-size: 20px;
    color: #370617;
    text-align: center;
}
.heart {
    font-size: 30px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Session state
if "step" not in st.session_state:
    st.session_state.step = 1

# STEP 1
if st.session_state.step == 1:
    st.markdown("<div class='title'>Hey You 🌸</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Someone has something special for you…</div>", unsafe_allow_html=True)
    st.markdown("<div class='heart'>💗 💗 💗</div>", unsafe_allow_html=True)

    if st.button("Take the first step 🌱"):
        st.session_state.step = 2

# STEP 2
elif st.session_state.step == 2:
    st.markdown("<div class='title'>A Little Closer 💕</div>", unsafe_allow_html=True)
    st.markdown("<div class='message'>Every rose has a story… and this one is just for you.</div>", unsafe_allow_html=True)

    if st.button("Reveal more 🌸"):
        st.session_state.step = 3

# STEP 3
elif st.session_state.step == 3:
    st.markdown("<div class='title'>Why You Matter 🌹</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='message'>
    You bring warmth like sunshine,<br>
    calm like a soft breeze,<br>
    and happiness without even trying.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Final Surprise 💝"):
        st.session_state.step = 4

# FINAL STEP
elif st.session_state.step == 4:
    st.balloons()
    st.markdown("<div class='title'>Happy Rose Day 🌹</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='subtitle'>
    Moitreyee ❤️
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='message'>
    This rose may be virtual,<br>
    but the feelings behind it are very real.<br><br>
    Always yours 💕
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='heart'>🌹 🌹 🌹</div>", unsafe_allow_html=True)
