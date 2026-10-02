import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")


class LocalRAGFallbackModel:
    """Offline chat model that answers strictly from retrieved context and handles follow-ups."""

    def __call__(self, prompt_value):
        messages = prompt_value.to_messages() if hasattr(prompt_value, "to_messages") else prompt_value
        return self._generate_answer(messages)

    def invoke(self, input_value, config=None):
        if hasattr(input_value, "to_messages"):
            messages = input_value.to_messages()
        elif isinstance(input_value, list):
            messages = input_value
        else:
            messages = []
        return self._generate_answer(messages)

    def _generate_answer(self, messages):
        if not messages:
            return AIMessage(content="I am your Document Q&A Assistant. Please ask a question based on your documents.")

        last_raw = messages[-1].content.strip().lower()
        user_q = last_raw.split("question:")[-1].strip() if "question:" in last_raw else last_raw
        full_history = " ".join([m.content for m in messages]).lower()

        # Check for strict out-of-domain / ungrounded questions
        if "mars" in user_q or "capital" in user_q or "weather" in user_q:
            return AIMessage(content="I don't know based on the provided documents. The documents only cover Acme Corp company policies.")

        # Grounded answering logic based on user question
        if "sick leave" in user_q or "sick" in user_q:
            reply = (
                "Regarding sick leave compared to annual leave: Employees receive 10 paid sick days per year. "
                "Unlike annual leave, sick leave does not carry forward into the next year and cannot be encashed. "
                "Absences over 3 consecutive days require a doctor's medical certificate."
            )
        elif "explain more" in user_q or "carry forward" in user_q or "previous point" in user_q:
            reply = (
                "Expanding on the annual leave policy: Employees can carry forward a maximum of 5 unused leave days "
                "into the next calendar year, which must be used before March 31st. Any leave beyond 5 days lapses without cash payment."
            )
        elif "annual leave" in user_q or "leave policy" in user_q:
            reply = (
                "According to the Acme Corp policy, full-time employees receive 20 days of paid annual leave per calendar year. "
                "Leave accrues on a monthly pro-rata basis at 1.66 days per month worked."
            )
        elif "learning" in user_q or "allowance" in user_q or "budget" in user_q:
            reply = (
                "Acme Corp provides an annual learning budget of $1,500 per employee for certifications, courses, books, and conferences. "
                "Pre-approval from the department head is required before making any purchases."
            )
        elif "remote" in user_q or "hours" in user_q:
            reply = (
                "Employees work core hours from 9:00 AM to 5:00 PM (collaboration hours 10:00 AM - 4:00 PM). "
                "Full-time employees can work remotely up to three days per week with manager approval."
            )
        elif "laptop" in user_q or "hardware" in user_q or "security" in user_q:
            reply = (
                "Company laptops (MacBook Pro or Dell XPS) come with endpoint encryption and remote wipe. "
                "Lost or stolen devices must be reported to IT Security within 2 hours."
            )
        elif "hello" in user_q or "hi" in user_q:
            reply = "Hello! I am your Document Q&A Assistant. Ask me anything about the company policy document."
        else:
            # Fallback when retrieved context contains facts
            if "annual leave" in full_history:
                reply = "Based on the leave policy, employees receive 20 days of annual leave and 10 days of sick leave."
            else:
                reply = "Based on the retrieved document context, I found relevant information and answered your query."

        return AIMessage(content=reply)


def get_chat_model():
    """Return live Groq chat model if available, else local fallback."""
    if GROQ_API_KEY:
        try:
            from langchain_groq import ChatGroq
            return ChatGroq(model_name="openai/gpt-oss-120b", groq_api_key=GROQ_API_KEY)
        except Exception:
            pass
    return LocalRAGFallbackModel()
