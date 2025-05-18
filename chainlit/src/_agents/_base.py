from chainlit import Message


class AgentWrapper():
    def __init__(self,
        model_host: str = "",
        model_url: str = "",
        model_name: str = "",
        mlflow_url = "",
    ):
        pass
    

    async def on_chat_start(self):
        pass


    async def on_message(self, input_message: Message):
        await Message(content="Not implemented").send()
