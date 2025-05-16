from chainlit import Message


class AgentWrapper():
    def __init__(self, host: str, model: str):
        pass
    

    async def on_chat_start(self):
        pass


    async def on_message(self, message: Message):
        await Message(content="Not implemented").send()
