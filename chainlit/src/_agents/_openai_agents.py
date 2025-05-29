from uuid import uuid4

from agents import Agent, AsyncOpenAI, ModelSettings, OpenAIChatCompletionsModel, Runner
from agents.mcp.server import MCPServerSse, MCPServerStreamableHttp
from chainlit import Message
from mlflow import set_experiment, set_tracking_uri
from mlflow.openai import autolog
from openai.types.responses import ResponseTextDeltaEvent
from openai.types.shared import Reasoning

from _agents._base import AgentWrapper as BaseAgent
from _tools._duckduckgo import news as duckduckgo_news, text as duckduckgo_text
from _tools._new_york_times import news as nyt_news
from _tools._wikipedia import search as wikipedia


class AgentWrapper(BaseAgent):
    def __init__(
        self,
        model_url: str = "",
        model_name: str = "",
        mlflow_url: str = "",
        **params,
    ):
        self.model_url = model_url
        self.model_name = model_name
        self.mlflow_url = mlflow_url
        self.experiment_id = str(uuid4())
        self.model: OpenAIChatCompletionsModel = None
        self.agent: Agent = None

    async def on_chat_start(self):
        set_tracking_uri(self.mlflow_url)

        self.model = OpenAIChatCompletionsModel(
            model=self.model_name,
            openai_client=AsyncOpenAI(
                api_key="dummy-api-key",
                base_url=self.model_url + "/v1",
            ),
        )

        playwright_mcp = MCPServerSse(
            name="Playwright MCP",
            params={
                "cache_tools_list": True,
                "client_session_timeout_seconds": 5.0,
                "url": "http://playwright:9000/sse",
            },
        )
        await playwright_mcp.connect()

        self.agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant.",
            model=self.model,
            model_settings=ModelSettings(
                tool_choice="auto",
                parallel_tool_calls=True,
                reasoning=Reasoning(
                    effort="high",
                    summary="auto",
                ),
            ),
            mcp_servers=[playwright_mcp],
            # tools=[nyt_news, wikipedia],
        )

    async def on_message(self, input_message: Message):
        autolog()
        set_experiment(self.experiment_id)
        result = await Runner.run(self.agent, input_message.content)

        output_message = Message(content=result.final_output)
        await output_message.send()

        # async for event in result.stream_events():
        #     print(event.type)
        #     if event.type == "raw_response_event" and isinstance(
        #         event.data, ResponseTextDeltaEvent
        #     ):
        #         print(event)
        #         await output_message.stream_token(event.data.delta)

        # await output_message.send()
