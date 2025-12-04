import requests
import json

MODEL_NAME = "llama3.1:8b"

def ask_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": True
    }

    with requests.post(
        "http://localhost:11434/api/generate",
        json=payload,
        stream=True
    ) as response:

        if response.status_code != 200:
            print("Error:", response.status_code)
            return

        full_response = ""
        for line in response.iter_lines():
            if line:
                content = line.decode("utf-8").removeprefix("data: ")
                try:
                    chunk = json.loads(content)
                    text = chunk.get("response", "")
                    print(text, end="", flush=True)
                    full_response += text
                except:
                    pass

        print("\n")
        return full_response


def chat():
    print("AI Chat Started. Type 'Bye' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            break

        print("AI: ", end="")
        ask_ollama(user_input)


if __name__ == "__main__":
    chat()
