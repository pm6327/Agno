from agno.agent import Agent

# from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama

from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
import os

# load keys
load_dotenv()
# defining llm
#  using ollama for testing purpose as it is free and easy to use, you can use any model of your choice
llm = Ollama(id="llama3")
# llm = OpenAIChat(
#     id="nousresearch/nous-hermes-2-mixtral:free",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
# )
# Create a database
db = SqliteDb(db_file="chat_history.db")

# build the agent
agent = Agent(
    name="My Agent",
    model=llm,
    db=db,
    session_id="session_1",
    user_id="user1",
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
    stream=True,
)

agent.print_response(
    input="Explain gen AI in 100 words in a simple way",
    session_id="session_1",
    user_id="user1",
)
