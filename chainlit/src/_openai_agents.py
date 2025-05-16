from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from chainlit import Message

class AgentWrapper():
    def __init__(self):
        self.model = OpenAIChatCompletionsModel(
            model="qwen3:0.6b",
            openai_client=AsyncOpenAI(
                api_key="dummy-api-key",
                base_url="http://ollama:11434/v1",
            ),
        )

        self.agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant.",
            model=self.model,
        )


    async def on_chat_start(self):
        pass


    async def on_message(self, message: Message):
        result = Runner.run_sync(self.agent, message.content)
        await Message(content=result.final_output).send()
