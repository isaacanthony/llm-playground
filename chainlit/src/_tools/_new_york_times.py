from agents import function_tool
from markitdown import MarkItDown


@function_tool
def business_news() -> str:
    """
    Get business news stories from the New York Times.

    Args:
    """
    return _get_nyt_rss_md("Business").text_content


@function_tool
def world_news() -> str:
    """
    Get world news stories from the New York Times.

    Args:
    """
    return _get_nyt_rss_md("World").text_content


def _get_nyt_rss_md(topic: str) -> str:
    return (
        MarkItDown()
        .convert(f"https://rss.nytimes.com/services/xml/rss/nyt/{topic}.xml")
        .text_content
    )
