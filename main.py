from openai import OpenAI

def main():
    message = 'Hello AI. What is up?'
    messages = [{"role": "user", "content": message}]
    ollama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
    model_name = "llama3.2:1b"

    response = ollama.chat.completions.create(model=model_name, messages=messages)
    answer = response.choices[0].message.content
    print(answer)


if __name__ == "__main__":
    main()