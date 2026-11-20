from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()

agent = Agent(
    "google:gemini-3.5-flash",
    system_prompt="You are a friendly assistant. Reply in the user's language.",
)

while True:
    user_message = input("You: ")
    if user_message.lower() in ("exit", "quit"):
        break
    result = agent.run_sync(user_message)
    print("Agent:", result.output)
