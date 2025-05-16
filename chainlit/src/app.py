import chainlit as cl

from _autogen import AgentWrapper as AutogenAgent
from _langchain import AgentWrapper as LangChainAgent
from _openai_agents import AgentWrapper as OpenAIAgent


HOST = "ollama"
MODEL = "qwen3:0.6b"


agent = AutogenAgent(HOST, MODEL)


@cl.on_chat_start
async def on_chat_start():
    await agent.on_chat_start()


@cl.on_message
async def on_message(message: cl.Message):
    await agent.on_message(message)
