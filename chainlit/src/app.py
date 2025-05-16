import chainlit as cl
from _openai_agents import AgentWrapper


agent = AgentWrapper()


@cl.on_chat_start
async def on_chat_start():
    await agent.on_chat_start()


@cl.on_message
async def on_message(message: cl.Message):
    await agent.on_message(message)
