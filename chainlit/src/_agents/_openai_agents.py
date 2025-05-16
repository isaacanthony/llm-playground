from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from chainlit import Message
from openai.types.responses import ResponseTextDeltaEvent

from _agents._base import AgentWrapper as BaseAgent
from _tools._wikipedia import search as wikipedia


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
            tools=[wikipedia],
        )


    async def on_message(self, input_message: Message):
        result = Runner.run_streamed(self.agent, input_message.content)

        output_message = Message(content="")

        async for event in result.stream_events():
            if (
                event.type == "raw_response_event"
                and isinstance(event.data, ResponseTextDeltaEvent)
            ):
                await output_message.stream_token(event.data.delta)

        await output_message.send()
