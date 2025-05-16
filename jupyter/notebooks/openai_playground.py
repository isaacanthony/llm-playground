from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

model = OpenAIChatCompletionsModel(
    model="qwen3:0.6b",
    openai_client=AsyncOpenAI(base_url="http://ollama:11434/v1", api_key="dummy-api-key"),
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model,
)

result = Runner.run_sync(agent, "Create a meal plan for a week.")
print(result.final_output)
