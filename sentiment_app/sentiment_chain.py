from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize model
llm = ChatOpenAI(
    model="llama-3.1-8b-instant",
    openai_api_key=GROQ_API_KEY,
    openai_api_base="https://api.groq.com/openai/v1"
)

# Prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Analyze the sentiment of the following text.
    Respond with ONLY one word: Positive, Negative, or Neutral.

    Text: {text}
    """
)

# Create chain
chain = LLMChain(llm=llm, prompt=prompt)

# Function to use in UI
def analyze_sentiment(text):
    result = chain.invoke({"text": text})
    return result["text"]