from json import dumps

from agents import function_tool
from duckduckgo_search import DDGS


@function_tool
def news(query: str) -> str:
    return dumps(DDGS().news(query))


@function_tool
def text(query: str) -> str:
    return dumps(DDGS().text(query))
