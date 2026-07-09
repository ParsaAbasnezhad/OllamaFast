from ollama import chat


# def ask_ai(prompt: str):
#     response = chat(
#         model="llama3.2",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )
#
#     return response["message"]["content"]


def stream_ai(prompt: str):
    stream = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True,
    )

    for chunk in stream:
        yield chunk["message"]["content"]