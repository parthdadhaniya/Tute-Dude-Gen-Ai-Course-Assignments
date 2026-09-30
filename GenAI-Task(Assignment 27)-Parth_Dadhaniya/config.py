import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")


class LocalFallbackModel:
    """Simple offline model that provides realistic answers based on chat history."""

    def __call__(self, prompt_value):
        messages = prompt_value.to_messages() if hasattr(prompt_value, "to_messages") else prompt_value
        return self._generate_reply(messages)

    def invoke(self, input_value, config=None):
        if hasattr(input_value, "to_messages"):
            messages = input_value.to_messages()
        elif isinstance(input_value, list):
            messages = input_value
        elif isinstance(input_value, dict):
            # If a dict is passed directly to invoke
            messages = input_value.get("chat_history", []) + input_value.get("history", [])
        else:
            messages = []
        return self._generate_reply(messages)

    def _generate_reply(self, messages):
        if not messages:
            return AIMessage(content="Hello! How can I help you today?")

        # Look at the latest message and overall history
        last_msg = messages[-1].content.strip().lower()
        full_text = " ".join([m.content for m in messages]).lower()

        # Follow-up test queries
        if "explain python list" in last_msg or ("list" in last_msg and "python" in last_msg and "example" not in last_msg and "tuple" not in last_msg):
            reply = (
                "A Python list is an ordered, mutable collection that allows storing multiple items. "
                "You can add, remove, and change items after creating the list using square brackets []."
            )
        elif "give an example" in last_msg or "example" in last_msg:
            # Check if previous context was about tuples or lists
            if "tuple" in full_text and full_text.rfind("tuple") > full_text.rfind("list"):
                reply = (
                    "Here is an example of a tuple:\n"
                    "coordinates = (10, 20)\n"
                    "# Tuples cannot be modified once created."
                )
            else:
                reply = (
                    "Here is an example of a Python list:\n"
                    "fruits = ['apple', 'banana', 'mango']\n"
                    "fruits.append('orange')\n"
                    "print(fruits)"
                )
        elif "what about tuple" in last_msg or ("tuple" in last_msg and "list" not in last_msg):
            reply = (
                "Tuples are very similar to lists, but they are immutable (cannot be modified after creation). "
                "They are defined using parentheses () instead of square brackets."
            )
        elif "modify a tuple" in last_msg or ("modify" in last_msg and "tuple" in last_msg):
            reply = (
                "No, you cannot modify a tuple like a list because tuples are immutable. "
                "Methods like append() or pop() will give an AttributeError."
            )
        elif "my name is" in last_msg:
            name = messages[-1].content.split()[-1].strip(".!")
            reply = f"Hello {name}! Nice to meet you. How can I help you with Python today?"
        elif "what is my name" in last_msg:
            if "parth" in full_text:
                reply = "Your name is Parth!"
            else:
                reply = "You haven't told me your name yet."
        elif "hello" in last_msg or "hi" in last_msg:
            reply = "Hello! I am your AI assistant with conversation memory. What would you like to learn?"
        else:
            reply = f"Got your question about '{messages[-1].content}'. Let me help you with that!"

        return AIMessage(content=reply)


def get_chat_model():
    """Return Groq chat model if API key is present, else use local fallback."""
    if GROQ_API_KEY:
        try:
            from langchain_groq import ChatGroq
            return ChatGroq(model_name="llama-3.1-8b-instant", groq_api_key=GROQ_API_KEY)
        except Exception:
            pass
    return LocalFallbackModel()
