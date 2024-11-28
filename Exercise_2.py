while True:
    prompt = prompt("Please enter the name of city you have visited: ")
    city = input(prompt)
    if city == "quit":
        break
    elif city == "S":
        print("You have visited the city of San Francisco!")
    elif city == "L":
        print("You have visited the city of Los Angeles!")
    elif city == "T":
        print("You have visited the city of Tokyo!")
    elif city == "Z":
        print("You have visited the city of Zurich!")
    elif city == "Y":
        print("You have visited the city of Yangon!") 
    else:
        print(f"I'd love to go too {city.title()}!")
        