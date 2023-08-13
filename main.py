import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are a doctor conversing with a patient during a medical consultation. The patient has come to you with concerns about their health and is seeking your professional advice and guidance.
."""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """
    if not state or "counter" not in state:
        state = {"counter": 0, "conversation": []}

    # Generate GPT-3.5 Turbo response
    if state["counter"] < 15:
        # Ask a question
        prompt = f"{SYSTEM_PROMPT}\n{''.join(state['conversation'])}\nWhat is the next question you ask?"
        bot_response = models.OpenAI.generate(
            system_prompt=prompt,
            message_history=message_history,
            model="gpt-3.5-turbo",
        )
        state["conversation"].append(f"Doctor: {bot_response}\n")
    else:
        # Give career advice
        prompt = f"{SYSTEM_PROMPT}\n{''.join(state['conversation'])}\nWhat medicine advice do you give?"
        bot_response = models.OpenAI.generate(
            system_prompt=prompt,
            message_history=message_history,
            model="gpt-3.5-turbo",
        )
        state["conversation"].append(f"Doctor: {bot_response}\n")

    state["counter"] += 1

    return bot_response, state
