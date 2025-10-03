def get_tool():
    tool = input("Enter a Cybersecurity tool (or type 'quit' to exit): ")
    return tool

def add_tool(tool_list, tool):
    tool_list.append(tool)
    print(f"This is a very powerful tool in Cybersecurity: {tool}")

def show_tools(tool_list):
    print("\nYour list of favorite cybersecurity tools:")
    for t in tool_list:
        print("-", t)
    print("\n")

def main():
    tools = []
    while True:
        tool = get_tool()
        if tool.lower() == "quit":
            break
        add_tool(tools, tool)
    show_tools(tools)

# Start the program
main()