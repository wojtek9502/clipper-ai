import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv(override=True)
OLLAMA_BASE_URL = os.environ["OLLAMA_BASE_URL"]
OLLAMA_API_KEY = os.environ["OLLAMA_API_KEY"]
OLLAMA_MODEL_NAME = os.environ["OLLAMA_MODEL_NAME"]

def main():
    message = 'Hello AI. What is up?. Tell me a long story about something'
    messages = [{"role": "user", "content": message}]
    ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key=OLLAMA_API_KEY)

    response = ollama.chat.completions.create(model=OLLAMA_MODEL_NAME, messages=messages)
    answer = response.choices[0].message.content
    print(answer)


if __name__ == "__main__":
    main()