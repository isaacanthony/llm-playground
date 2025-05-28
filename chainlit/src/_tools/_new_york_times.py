from enum import Enum

from agents import function_tool
from markitdown import MarkItDown


class NewsTopic(Enum):
    # World
    WORLD = "World"
    AFRICA = "Africa"
    AMERICAS = "Americas"
    ASIA_PACIFIC = "AsiaPacific"
    EUROPE = "Europe"
    MIDDLE_EAST = "MiddleEast"
    # US
    US = "US"
    EDUCATION = "Education"
    POLITICS = "Politics"
    # Business
    BUSINESS = "Business"
    ECONOMY = "Economy"
    # Technology
    TECHNOLOGY = "Technology"
    # Sports
    SPORTS = "Sports"
    # Science
    SCIENCE = "Science"


@function_tool
def news(topic: NewsTopic) -> str:
    """
    Get recent news stories from the New York Times.

    Args:
        topic: The topic of news being requested.
    """
    return (
        MarkItDown()
        .convert(f"https://rss.nytimes.com/services/xml/rss/nyt/{topic.value}.xml")
        .text_content
    )
