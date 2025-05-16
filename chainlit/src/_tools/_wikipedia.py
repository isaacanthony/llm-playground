from agents import function_tool
from wikipedia import summary


@function_tool
def search(query: str) -> str:
    return summary(query)
