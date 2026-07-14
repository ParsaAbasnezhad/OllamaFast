import ollama


class OllamaService:

    @staticmethod
    def chat(messages: list[dict]) -> str:

        response = ollama.chat(
            model="llama3.2",
            messages=messages
        )

        return response["message"]["content"]