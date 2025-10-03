favorite_cybersecurity_tools = ["Wireshark", "Burpsuite", "Autopsy"]

while True:
    name = input("Enter your name (or type 'quit' to exit): ")
    if name.lower() == "quit":
        print("Exiting Cyber Lab access program. Final tools list:")
        for tool in favorite_cybersecurity_tools:
            print("-", tool)
        break

    # Validate age input
    while True:
        try:
            age = int(input(f"Hello {name}, enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for age.")

    # Check access
    if age >= 18:
        print(f"{name}, you can have access to the Cyber Lab")
    else:
        print(f"Sorry {name}, you must be 18 or older.")

    # Add favorite tool
    tool = input("Enter your favorite cybersecurity tool: ")
    favorite_cybersecurity_tools.append(tool)

    # Show updated list
    print("\nUpdated tools list:")
    for tool in favorite_cybersecurity_tools:
        print("-", tool)

    # Option to remove a tool
    remove_choice = input("\nDo you want to remove a tool from the list? (yes/no): ").lower()
    if remove_choice == "yes":
        tool_to_remove = input("Enter the tool you want to remove: ")
        if tool_to_remove in favorite_cybersecurity_tools:
            favorite_cybersecurity_tools.remove(tool_to_remove)
            print(f"{tool_to_remove} has been removed.")
        else:
            print(f"{tool_to_remove} is not in the list.")

    # Show final list after removal
    print("\nCurrent tools list:")
    for tool in favorite_cybersecurity_tools:
        print("-", tool)
    print("\n")  # spacing