from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.ollama import OllamaChatCompletionClient
from chainlit import Message

from _base import AgentWrapper as BaseAgent


class AgentWrapper(BaseAgent):
    def __init__(self, host: str, model: str):
        self.model_client = OllamaChatCompletionClient(
            host=host,
            model=model,
            model_info={
                "family": model,
                "function_calling": True,
                "json_output": True,
                "multiple_system_messages": True,
                "structured_output": True,
                "vision": True,
            },
        )

        self.agent = AssistantAgent(
            "Assistant",
            model_client=self.model_client,
        )


    async def on_message(self, message: Message):
        result = await self.agent.run(task=message.content)
        await Message(content=result.messages[-1].content).send()
