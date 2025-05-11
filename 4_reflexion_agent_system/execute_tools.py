import json
from typing import List
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langchain_community.tools import TavilySearchResults

# Create the Tavily search tool
tavily_tool = TavilySearchResults(max_results=5)


def execute_tools(state: List[BaseMessage]) -> List[BaseMessage]:
    last_ai_message: AIMessage = state[-1]

    # If there were no tool_calls, nothing to append
    if not getattr(last_ai_message, "tool_calls", None):
        return []

    tool_messages: List[ToolMessage] = []

    for tool_call in last_ai_message.tool_calls:
        name = tool_call["name"]
        call_id = tool_call["id"]

        # Only handle AnswerQuestion and ReviseAnswer for now
        if name not in ["AnswerQuestion", "ReviseAnswer"]:
            continue

        search_queries = tool_call["args"].get("search_queries", [])

        # Run each query
        query_results = {}
        for q in search_queries:
            query_results[q] = tavily_tool.invoke(q)

        # Build the ToolMessage with name, tool_call_id, and content
        tool_messages.append(
            ToolMessage(
                name=name,
                tool_call_id=call_id,
                content=json.dumps(query_results),
            )
        )

    return tool_messages
