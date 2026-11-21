from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()

SYSTEM_PROMPT = """
You are "Coach Py", a Python study buddy for beginners.
Your tone is warm, encouraging and simple.
Never write the fullolution to a homework or task; give hints instead.
Reply in the english language.
"""

agent = Agent("google:gemini-3.5-flash-lite", system_prompt=SYSTEM_PROMPT)

while True:
    user_message = input("You: ")
    if user_message.lower() in ("exit", "quit"):
        print("Agent: welcome 👋")
        break
    result = agent.run_sync(user_message)
    print("Agent:", result.output)
