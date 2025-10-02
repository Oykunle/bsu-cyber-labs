tools = ["Wireshark", "Burp Suite", "Nmap"]

name = input("What is your name? ")
favorite_tool = input("What is your favorite tool? ")

tools.append(favorite_tool)

print(f"Hello, {name}! Welcome to the Cyber Lab.")

print("Here is the updated list of cybersecurity tools:")
for tool in tools:
    print("-", tool)
