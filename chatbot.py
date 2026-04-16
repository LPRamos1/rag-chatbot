from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def stream_response(messages):
    """
    Sends messages to the LLM and streams the response.

    Args:
        messages (list): List of system/user messages
    """
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # or llama-3.3-70b-versatile
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
    print()
