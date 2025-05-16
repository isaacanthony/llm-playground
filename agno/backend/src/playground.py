from agno.agent import Agent
from agno.models.ollama import OllamaTools
from agno.playground import Playground, serve_playground_app
from agno.tools.duckduckgo import DuckDuckGoTools


agent = Agent(
    name="DuckDuckGo Researcher",
    model=OllamaTools(host="ollama", id="qwen3:0.6b"),
    tools=[DuckDuckGoTools()],
    reasoning=True,
    show_tool_calls=True,
    markdown=True,
    telemetry=False,
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", host="0.0.0.0", reload=True)
