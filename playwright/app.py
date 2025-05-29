from io import BytesIO

from fastmcp import FastMCP
from markitdown import MarkItDown
from playwright.async_api import async_playwright


mcp = FastMCP("PlayWright MCP")


@mcp.tool()
async def goto(url: str) -> str:
    """
    Navigates to the given URL and returns the page content as markdown.

    Args:
        url: The URL to navigate to.
    """
    page_html = ""

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_load_state()
        page_html = await page.content()
        await browser.close()

    return _to_markdown(page_html)


def _to_markdown(input_str: str) -> str:
    input_file = BytesIO(input_str.encode("utf-8"))
    return MarkItDown().convert(input_file).text_content
