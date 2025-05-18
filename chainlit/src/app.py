import chainlit as cl

from _agents._autogen import AgentWrapper as AutogenAgent
from _agents._langchain import AgentWrapper as LangChainAgent
from _agents._openai_agents import AgentWrapper as OpenAIAgent


MODEL_HOST = "ollama"
MODEL_NAME = "qwen3:0.6b"
MLFLOW_URL = "http://mlflow:8080"


agent = OpenAIAgent(
    model_host=MODEL_HOST,
    model_url=f"http://{MODEL_HOST}:11434",
    model_name=MODEL_NAME,
    mlflow_url=MLFLOW_URL,
)


@cl.on_chat_start
async def on_chat_start():
    await agent.on_chat_start()


@cl.on_message
async def on_message(message: cl.Message):
    await agent.on_message(message)
