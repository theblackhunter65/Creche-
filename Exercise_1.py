message = " "
while message != "q":
    message = input("Enter a message (or 'q' to quit): ")
    if message == "q":
        break
    elif message == "h":
        print("Help:")
        print("  h: display this help message")
    elif message == "m":
        print("Message:")
        print("  m: display this message")
    elif message == "G":
        print("Goodbye!")
    else:
        print("Invalid input. Please try again.")