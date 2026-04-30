import streamlit as st
from sentiment_chain import analyze_sentiment

# Page config
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 AI Sentiment Analyzer")
st.markdown("Enter text and get instant sentiment analysis 🚀")

# Input box
user_input = st.text_area("Enter your text here:", height=150)

# Button
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_sentiment(user_input)

        # Display result nicely
        if "Positive" in result:
            st.success(f"😊 Sentiment: {result}")
        elif "Negative" in result:
            st.error(f"😡 Sentiment: {result}")
        else:
            st.info(f"😐 Sentiment: {result}")

# Footer
st.markdown("---")
st.caption("Built with LangChain + Groq + Streamlit")