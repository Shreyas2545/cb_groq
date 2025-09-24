import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access your secret keys
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables!")

def chatbot():
    print("Hello! I am your chatbot. Type 'exit' or 'quit' to stop.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Send request to GROQ API
        try:
            response = requests.post(
                "https://api.groq.ai/v1/engines/default/completions",  # replace if your endpoint is different
                headers={"Authorization": f"Bearer {groq_api_key}"},
                json={
                    "prompt": user_input,
                    "max_output_tokens": 100
                }
            )
            response.raise_for_status()
            data = response.json()
            
            # Extract the text from response
            output_text = data.get("output_text") or data.get("completions", [{}])[0].get("text", "")
            
            print("Bot:", output_text)
        
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chatbot()
