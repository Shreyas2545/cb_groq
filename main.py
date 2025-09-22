import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access your secret keys
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    print("Hello! I am your chatbot.")
    user_input = input("You: ")
    print(f"Your message was: {user_input}")
    print(f"(Using GROQ key: {groq_api_key[:4]}****)")

if __name__ == "__main__":
    chatbot()
