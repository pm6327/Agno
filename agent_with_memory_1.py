from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.in_memory import InMemoryDB
from dotenv import load_dotenv

# because of some problem in agno version not able to execute code properly


# load the api keys from .env file
load_dotenv()

# create the model
# this gpt model is paid so it won't give any output
llm = OpenAIChat(id="gpt-4.1-mini")
# Session id for giving memory to agent

session_id = "session_1"
# Create a Database
# this db is only used for demo
db = InMemoryDB()

# create the agent
agent = Agent(
    model=llm,
    db=db,
    session_id=session_id,
    add_history_to_context=True,
    num_history_runs=3,
    name="Agent with Memory",
    stream=True,
    markdown=True,
)

# give inputs to the agent

agent.print_response(input="What is the capital of France?")

agent.print_response(input="What is the capital of Germany?")
messages = agent.get_chat_history(session_id)

for message in messages:
    role, content = message.role, message.content
    if role == "system":
        continue
    else:
        print(f"Role:{role} , Message: {content}")
