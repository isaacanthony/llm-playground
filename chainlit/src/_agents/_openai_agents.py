from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from chainlit import Message
from mlflow import set_experiment, set_tracking_uri
from mlflow.openai import autolog
from openai.types.responses import ResponseTextDeltaEvent
from uuid import uuid4

from _agents._base import AgentWrapper as BaseAgent
from _tools._duckduckgo import news as duckduckgo_news, text as duckduckgo_text
from _tools._wikipedia import search as wikipedia


class AgentWrapper(BaseAgent):
    def __init__(
        self,
        model_url: str = "",
        model_name: str = "",
        mlflow_url: str = "",
        **params,
    ):
        self.experiment_id = str(uuid4())
        set_tracking_uri(mlflow_url)

        self.model = OpenAIChatCompletionsModel(
            model=model_name,
            openai_client=AsyncOpenAI(
                api_key="dummy-api-key",
                base_url=model_url + "/v1",
            ),
        )

        self.agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant.",
            model=self.model,
            tools=[duckduckgo_news, duckduckgo_text, wikipedia],
        )

    async def on_message(self, input_message: Message):
        autolog()
        set_experiment(self.experiment_id)
        result = Runner.run_streamed(self.agent, input_message.content)

        output_message = Message(content="")

        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                await output_message.stream_token(event.data.delta)

        await output_message.send()
