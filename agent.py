from agno.agent import Agent

from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

# load keys
load_dotenv()
# defininf llm
llm = OpenAIChat(
    id="gpt-5-mini",
    # model is paid so it won't give any o/p
)
# build the agent
agent = Agent(name="My Agent", model=llm, markdown=True)

agent.print_response(input="generate a 100 word summary on iran and US war")
