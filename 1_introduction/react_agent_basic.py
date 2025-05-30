from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
import datetime

load_dotenv()
  
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

search_tool = TavilySearchResults(search_depth='basic')

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """
    Get the current system time in the specified format.
    """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

tools = [search_tool,get_system_time]


agent = initialize_agent(tools=tools, llm=llm, agent='zero-shot-react-description', verbose=True)

agent.invoke("when was SpaceX's last launch and how many days ago was that from this instant?")

# result = agent.invoke("Give me a the weather forecast for Avon, Connecticut for the next 7 days. Include the temperature, humidity, and wind speed.")
# print(result)