from agno.agent import Agent
from agno.models.ollama import OllamaTools
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OllamaTools(host="ollama", id="qwen3:0.6b"),
    tools=[DuckDuckGoTools()],
    reasoning=True,
    show_tool_calls=True,
    markdown=True,
    telemetry=False,
)

agent.print_response("What is happening in France?", stream=True)
