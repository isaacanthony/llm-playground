from chainlit import LangchainCallbackHandler, Message, make_async, user_session
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from langchain_ollama.llms import OllamaLLM

from _base import AgentWrapper as BaseAgent


class AgentWrapper(BaseAgent):
    def __init__(self, host: str, model: str):
        self.model =  OllamaLLM(
            base_url=f"http://{host}:11434",
            model=model,
        )


    async def on_chat_start(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions.",
                ),
                ("human", "{question}"),
            ]
        )
        runnable = prompt | self.model | StrOutputParser()
        user_session.set("runnable", runnable)


    async def on_message(self, message: Message):
        runnable = user_session.get("runnable")

        msg = Message(content="")

        for chunk in await make_async(runnable.stream)(
            {"question": message.content},
            config=RunnableConfig(callbacks=[LangchainCallbackHandler()]),
        ):
            await msg.stream_token(chunk)

        await msg.send()
