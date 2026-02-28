from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from .data_loader import load_data

def create_agent():
    df = load_data()
    llm = ChatOpenAI(temperature=0)

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True
    )

    return agent