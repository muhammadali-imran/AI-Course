import os
import math

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )

@tool
def calculator(expression: str) -> str:
    """Evaluates a mathematical expression (e.g., '2 + 2', '15 * 4') and returns the result."""
    try:
        return str(eval(expression, {"__builtins__": None}, {}))
    except Exception as e:
        return f"Error: {e}"

@tool
def word_length(word: str) -> str:
    """Returns the character length of a given word or string."""
    return str(len(word))


@tool
def factorial(number: int) -> str:
    """Calculates the factorial of a non-negative integer."""
    if number < 0:
        return "Error: Factorial is only defined for non-negative integers."
    return str(math.factorial(number))


agent = create_agent(
    model=llm,
    tools=[calculator, word_length, factorial],
    system_prompt=(
        "You are a helpful assistant. Use the provided tools whenever they are "
        "appropriate, especially for calculations."
    ),
)


def _message_text(content: object) -> str:
    """Extract readable text from plain or Gemini structured message content."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    return str(content)


def run_agent(user_input: str) -> None:
    """Run one request and print a readable trace of the agent's work."""
    print(f"\n[user] {user_input}")
    for update in agent.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        stream_mode="updates",
    ):
        for node_name, state_update in update.items():
            for message in state_update.get("messages", []):
                if isinstance(message, AIMessage) and message.tool_calls:
                    for tool_call in message.tool_calls:
                        print(
                            f"[tool call] {tool_call['name']}"
                            f"  arguments={tool_call['args']}"
                        )
                elif isinstance(message, ToolMessage):
                    print(f"[tool result] {message.name}: {message.content}")
                elif isinstance(message, AIMessage) and message.content:
                    print(f"[assistant] {_message_text(message.content)}")


if __name__ == "__main__":
    print("Welcome (type 'exit' to quit):")
    while True:
        user_input = input("your query: ")
        if user_input.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break
        try:
            run_agent(user_input)
        except Exception as error:
            print(f"[error] {error}")


