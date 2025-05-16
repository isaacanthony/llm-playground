from json import dumps

from agents import function_tool
from duckduckgo_search import DDGS


@function_tool
def news(query: str) -> str:
    """
    Search DuckDuckGo for current news stories related to a query.

    Args:
        query: The news query to search DuckDuckGo for.
    """
    return dumps(DDGS().news(query))


@function_tool
def text(query: str) -> str:
    """
    Search DuckDuckGo for pages related to a query.

    Args:
        query: The query to search DuckDuckGo for.
    """
    return dumps(DDGS().text(query))
