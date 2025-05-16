from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from chainlit import Message

from _base import AgentWrapper as BaseAgent


class AgentWrapper(BaseAgent):
    def __init__(self, host: str, model: str):
        self.model = OpenAIChatCompletionsModel(
            model=model,
            openai_client=AsyncOpenAI(
                api_key="dummy-api-key",
                base_url=f"http://{host}:11434/v1",
            ),
        )

        self.agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant.",
            model=self.model,
        )


    async def on_message(self, message: Message):
        result = Runner.run_sync(self.agent, message.content)
        await Message(content=result.final_output).send()
