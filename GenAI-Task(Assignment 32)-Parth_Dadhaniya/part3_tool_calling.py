# Part 3: Tool Binding & Tool Calling Flow (Tasks 5 & 6)
# Student: Parth Dadhaniya

from config import get_llm
from part2_custom_tools import get_company_toolkit


def execute_tool_call(query, llm_with_tools, tools_by_name):
    print(f"\nUser Query: '{query}'")
    ai_msg = llm_with_tools.invoke(query)

    # Check if the model decided to call tools
    if ai_msg.tool_calls:
        print("Model chose to call tool:")
        for call in ai_msg.tool_calls:
            tname = call["name"]
            targs = call["args"]
            print(f"  -> Tool: {tname}, Arguments: {targs}")

            if tname in tools_by_name:
                output = tools_by_name[tname].invoke(targs)
                print(f"  -> Tool Execution Result: {output}")

        print("Final response generated based on tool output.")
    else:
        print(f"Direct Response: {ai_msg.content}")


def main():
    print("--- Task 5: Tool Binding to LLM ---")
    tools = get_company_toolkit()
    tools_by_name = {t.name: t for t in tools}

    llm = get_llm()
    # Bind tools to the model
    llm_with_tools = llm.bind_tools(tools)
    print(f"Bound {len(tools)} tools: {[t.name for t in tools]}")

    print("\n--- Task 6: Demonstrating Tool Calling Flow ---")
    # Math query
    execute_tool_call("Calculate 15 * 8", llm_with_tools, tools_by_name)
    # Policy query
    execute_tool_call("What is our company leave policy?", llm_with_tools, tools_by_name)


if __name__ == "__main__":
    main()
