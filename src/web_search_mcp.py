# src/web_search_mcp.py
import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.tools import tool
import logging

logger = logging.getLogger(__name__)

async def _load_brave_tool():
    """
    Implement the MCP client connection for Brave search with proper error handling.
    """
    brave_api_key = os.environ.get("BRAVE_API_KEY", "")
    
    if not brave_api_key:
        logger.warning("BRAVE_API_KEY not found in environment variables. Web search will be unavailable.")
        
        @tool
        def web_search_unavailable(query: str) -> str:
            """Fallback tool when web search is unavailable due to missing API key."""
            return (
                "Web search is currently unavailable because BRAVE_API_KEY is not configured. "
                "Please set the BRAVE_API_KEY environment variable to enable web search functionality."
            )
        
        return [web_search_unavailable]
    
    try:
        logger.info("Initializing Brave MCP client...")
        
        client = MultiServerMCPClient({
            "brave_search": {
                "command": "npx",
                "args": [
                    "-y",
                    "@brave/brave-search-mcp-server",
                    "--transport",
                    "stdio",
                    "--brave-api-key",
                    brave_api_key
                ],
                "transport": "stdio"
            }
        })
        
        all_tools = await client.get_tools()
        
        brave_tools = [
            tool for tool in all_tools 
            if "brave" in tool.name.lower()
        ]
        
        if not brave_tools:
            logger.warning("No Brave tools found from MCP server.")
            raise ValueError("No Brave tools available from MCP server")
        
        logger.info(f"Successfully loaded {len(brave_tools)} Brave tool(s): {[t.name for t in brave_tools]}")
        return brave_tools
    
    except Exception as e:
        logger.error(f"Failed to initialize Brave MCP client: {str(e)}", exc_info=True)
        
        @tool
        def web_search_error(query: str) -> str:
            """Fallback tool when web search initialization fails."""
            return (
                f"Web search is currently unavailable due to an error: {str(e)}. "
                "Please check your BRAVE_API_KEY and ensure the MCP server is properly configured."
            )
        
        return [web_search_error]

def get_brave_web_search_tool_sync():
    """Safe sync wrapper for Streamlit."""
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = None
    
    if loop and loop.is_running():
        return loop.run_until_complete(_load_brave_tool())
    else:
        return asyncio.run(_load_brave_tool())