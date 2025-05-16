from agents import function_tool
from wikipedia import summary


@function_tool
def search(query: str) -> str:
    """
    Search Wikipedia for a provided query.

    Args:
        query: The query to search Wikipedia for.
    """
    return summary(query)
