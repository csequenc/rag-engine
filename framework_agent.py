from framework_planner import plan
from framework_tools import calculate, rag_search
from framework_utils import build_tool_descriptions
from framework_tools import get_weather


# Single source of truth
tools = [
    calculate,
    get_weather,
    rag_search
]

# Automatically build tool descriptions for the planner
tool_descriptions = build_tool_descriptions(tools)

# Automatically build the tool registry
tool_registry = {
    tool.name: tool
    for tool in tools
}


def run(query: str):

    # Ask the planner which tool to use
    decision = plan(query, tool_descriptions)

    print("Planner Decision:", decision)

    # Find the selected tool
    tool = tool_registry.get(decision.tool)

    if tool is None:
        raise ValueError(f"Unknown tool selected: {decision.tool}")

    # Execute the tool
    result = tool.invoke(decision.input)

    return result


if __name__ == "__main__":

    result = run("What is the weather in Delhi?")

    print(result)