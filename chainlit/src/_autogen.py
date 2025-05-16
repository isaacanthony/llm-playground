from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
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


    async def on_message(self, input_message: Message):
        output_message = Message(content="")

        async for result in self.agent.run_stream(task=input_message.content):
            if isinstance(result, TextMessage):
                await output_message.stream_token(result.content)

        await output_message.send()
