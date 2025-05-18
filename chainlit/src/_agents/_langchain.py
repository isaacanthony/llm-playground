from chainlit import LangchainCallbackHandler, Message, make_async, user_session
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain_ollama.llms import OllamaLLM

from _agents._base import AgentWrapper as BaseAgent


class AgentWrapper(BaseAgent):
    def __init__(
        self,
        model_url: str = "",
        model_name: str = "",
        **params,
    ):
        self.model = OllamaLLM(
            base_url=model_url,
            model=model_name,
        )

    async def on_chat_start(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                        You're a very knowledgeable historian who provides accurate
                        and eloquent answers to historical questions.
                    """,
                ),
                ("human", "{question}"),
            ]
        )
        runnable = prompt | self.model | StrOutputParser()
        user_session.set("runnable", runnable)

    async def on_message(self, input_message: Message):
        runnable = user_session.get("runnable")

        output_message = Message(content="")

        for chunk in await make_async(runnable.stream)(
            {"question": input_message.content},
            config=RunnableConfig(callbacks=[LangchainCallbackHandler()]),
        ):
            await output_message.stream_token(chunk)

        await output_message.send()
