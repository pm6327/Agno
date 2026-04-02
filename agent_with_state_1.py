from agno.agent import Agent
from agno.models.ollama import Ollama
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
import os

load_dotenv()

llm = Ollama(id="llama3")
db = SqliteDb(db_file="session_state_db/temp.db")

# give a session id and user id to maintain the state of the conversation

session_id = "1"
user_id = "user_a"
# Create a session state for the agent
user_info = {"name": "Prakhar", "age": 22}
# Create an agent
agent = Agent(
    model=llm,
    name="agent with state",
    session_state=user_info,
    session_id=session_id,
    user_id=user_id,
    add_session_state_to_context=True,
    db=db,
    stream=True,
    markdown=True,
)

print(
    agent.print_response(
        "tell me my name and age",
        session_id=session_id,
        user_id=user_id,
    )
)
