# print("I love pizza ")
# print("It's really good !")

# name = input("Enter your name :")
# age =  int(input("Enter your age :"))
# age = int(age)
# age = age+1
# print(f"Hello {name}")
# print(f"You are {age} years old")

# adjective1 = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# adjective2 = input("Enter an adjective:")
# verb = input("Enter a verb : ")
# adjective3 = input("Enter an adjetictive: ")


# print(f"Today I want to a {adjective1} zoo")
# print(f"In an exhibit, I saw {noun}")
# print(f"{noun} was {adjective2} and {verb} ing ")
# print(f"I was {adjective3}")


# length = float(input("Enter the legth of a rectangle : "))
# width = float(input("Enter the width of a rectangle  : "))
# height =float(input("Enter the height of a rectangle : "))

# volume = length*width*height

# print(f"The volume is : {volume} cm^3")


# item = input("What item would you like to buy :")
# price = float(input("what is the price ? :"))
# quantity = int(input("How many would you like ? : "))

# total = price * quantity

# print(f"You have bought{quantity} x {item}/s")

# print(f"Your total is : ${round(total, 2)}")

# friends = 0 

# friends = friends + 1
# friends += 1 

# friends = friends - 2

# friends -= 2
  
# friends = friends -3
# friends *=3 
# friends = friends / 2 
# friends = friends **2
# friends = friends % 3 

# print(friends)

# x = 3.14
# y = 4
# z = 5

# result = round (x)
# result = abs(y)
# result = pow(4,3)
# result = max(x,y,z)
# result = min(x,y,z)
# print(result)

# import math 

# x = 9.1

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)


# import math 

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference,2)}cm")



# import math 

# radius = float(input("Enter the radius of  a circle: "))


# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area)}cm^2")

# if = Do some code only If some codition is True 
#       Else do something else 

# age = int(input("Enter your age: "))

# if age < 0:
#     print("You are not born yet")
# elif age >= 100:
#     print("You are very old")
# elif age >= 18:
#     print("You are an adult")
# elif age >= 13:
#     print("You are a teenager")
# else:
#     print("You are a kid")






# for_sale = True 

# if for_sale:
#     print("This item is for sale: ")
# else:
#     print("This item is not for sale: ")




# for_sale = False

# if for_sale:
#     print("This item is for sale: ")
# else:
#     print("This item is not for sale: ")





# online = True 

# if online : 
#     print("The user is online: ")
# else:
#     print("The user is offline: ")



# online = False

# if online : 
#     print("The user is online: ")
# else:
#     print("The user is offline: ")



# operator = input("Enter an operator(+ - * /)")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2st number: "))

# if operator == "+":
#     result = num1 + num2
#     print((round(result , 3)))
# elif operator == "-":
#     result = num1 -num2
#     print((round(result , 3)))
# elif operator == "*":
#     result = num1 * num2
#     print((round(result , 3)))
# elif operator == "/":
#     result = num1 / num2
#     print((round(result , 3)))
# else:
#     print(f"{operator}is invalid operator")


# Python Weigh Converter 

# weight = float(input("Enter your weight "))
# unit = input("Kilogramas or Pounds ? (K or L):")
# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {weight, 1} {unit}")
# elif unit == "L" :
#     weight = weight / 2.205
#     unit = "kgs."   
#     print(f"Your weight is: {weight, 1} {unit}")
# else:
#     print(f"{unit} was not valid")






# Python temperature conversion program
#The Day is Monday 15/07/2024

# unit = input("Is this temperature in Celsius or Fahrenheit (C/F):  ")
# temp = float(input("Enter the temperature:  "))

# if unit == "C":
#     temp = round(temp * 9/5) + 32
#     print(f"The temperature in Fahrenheit is: {temp}°F")
# elif unit == "F":
#     temp = round(((temp - 32)) * 5 / 9, 1)
#     print(f"The temperature in Celsius is:{temp}°C")
# else:
#     print(f"{unit} is an invalid unit of measurement")

# logical operators = used on conditional statements 

#  and = checks two or more contditions if True 
#  or =  checks if at least one conditions is True
#  not = True if condition is False, and vice versa


# temp = 25

# if temp > 0 and temp < 30:
#     print("The temperature is good ")
# else:
#     print("The temperature is not good is bad")



# temp = 40
# sunny = False 
# if temp > 0 or temp < 30:
#     print("The temperature is good ")
# else:
#     print("The temperature is not good is bad")

# if not sunny:
#     print("It is cloudy outside ")
# else:
#     print("It is cloudy outside")



# Condition expression = A one-line shortcut for the  if-else statement (ternary operator)
#                   Prisnt or assingn one of two valurs based on a condition 
#                   X if condition else Y

# num = -5
# a = 6
# b = 7
# age = 13 
# temperature = 30 
# user_role = "guest"
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "0DD"

# print(result)


# max_num = a if a > b else b 
# min_num = a if a < b else b
# status = "Afut " if age >= 18 else "Child"
# wether= "HOT" if temperature > 20 else "C"
# print(status)
# print(wether)
# acess_level = "Full Acess" if user_role == "admin" else "Limited Access"
# print(acess_level)

# name = input("Enter your full name: ")

# phone_number = input("Enter your phone #: ")


# result = len(name)
# result = name.find ("o")
# result = name.find ("q")
# name = name.capitalize()
# print(name) 
# print(result)
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-" , "")
# phone_number = phone_number.replace("-", "")
# print(phone_number)

# print(help(str))

# validate usar input exercise 

# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits 
 
# username = input ("Enter a username:")

# if len(username) > 12:
#    print("Your username can't be more than 12 characters ")
# else:
#    print(f"Welcome {username}")



# user_name = input("Enter a username:")



# if len(user_name) > 12:
#     print("Your user can be more than 12 characters")
# elif not user_name.find("") == -1:
#     print("Your username can't contain spaces")
# else:
#     print(f"Welcome {user_name}")
    


# if len(user_name) > 12: 
#     print("Your user can be more than 12 characters")
# elif not user_name.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {user_name}")


# indexing = accssing elements of a sequence using [] (indexing operatos)
#                [start : end : step]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[3])

# print(credit_number[4])

# print(credit_number[5:9])
# print(credit_number[])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# print(credit_number)


# email = input("Enter your email: ")

# index = email.index("@")

# username = email[:index]
# domain = email[index + 1:] 

# print(f"Your username is {username} and domain is {domain}")


# format spaciers = {value:flags} format a value based on what
#             flags are inserted

# price1 = 3.14552
# price2 = -765.65
# price3 = 12.95

# print(f"Price 1 is {price1:.3f}")
# print(f"Price 2 is {price2:.3f}")
# print(f"price 3 is {price3:.3f}")

# price1 = 5.14567
# price2 = -765.53
# price3 =  12.34

# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")

# price1 = 5.14567
# price2 = -765.53
# price3 =  12.34

# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")

# price1 = 5.14567
# price2 = -765.53
# price3 =  12.34

# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")


# price1 = 5.14567
# price2 = -765.53
# price3 =  12.34

# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")

# price1 = 50000.14567
# price2 = -7650.53
# price3 =  1200.34

# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")


# price1 = 50000.14567
# price2 = -7650.53
# price3 =  1200.34

# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")


# While loop = execute some code WHILE some condition remains true 

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}")


# age = int(input("Enter your age: "))

# while age < 0 or age > 120: 
#     print("Invalid age")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# name = input("Enter your name: ")


# while name  == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}")



# age = int(input("Enter your age: "))

# while age < 0 or age > 120:
#     print("Invalid age ")
#     age = int(input("Enter your name: "))
# else:
#     print(f"You are {age} years old")


# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you are done and like it  {food} ")
#     food = input("Enter another food you like")



# print("Bye a see later")


#Exemple 3 

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print("Invalid {num}")
#     num = int(input("Enter a # between 1 - 10: "))
# else: 
#     print(f"Your number is {num}")





# Python compound interest calculator 

# principle = 0
# rate = 0 
# time = 0 

# while principle <= 0:
#     principle = float(input("Enter the priciple amount:"))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero:")
        



# # print(principle)

# while rate <= 0:
#     rate = float(input("Enter the interest rate :"))
#     if rate <= 0:
#         print("Interest rate  can't be less than or equal to zero:")




# while time <= 0:
#     time = float(input("Enter the interest time :"))
#     if time <= 0:
#         print("Interest Time can't be less than or equal to zero:")


# # print(principle)
# # print(rate)
# # print(time)

# total = principle * pow((1+rate/100 ),time)
# print(f"Balance after{time} year/s:${total:.2f}")

# principle = 0
# rate = 0 
# time = 0 

# while True:
#     principle = float(input("Enter the priciple amount:"))
#     if principle < 0:
#         print("Principle can't be less than  zero:")
#     else:
#         break



# print(principle)

# while True:
#     rate = float(input("Enter the interest rate :"))
#     if rate < 0:
#         print("Interest rate  can't be less than zero:")
#     else:
#         break



# while True < 0:
#     time = float(input("Enter the interest time :"))
#     if time < 0:
#         print("Interest Time can't be less than  zero:")
#     else:
#         break


# # print(principle)
# # print(rate)
# # print(time)

# total = principle * pow((1+rate/100 ),time)
# print(f"Balance after{time} year/s:${total:.2f}")


# for loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, etc.

# credit_carf = "1234-5678-3456"

# for x in reversed(range(1,11,3)):
#     print(x)

# print("HAPPY NEW YEAR ")

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13:
#         break
#     else:
#         print(x)

# for x in range(1,11):
#     if x == 13: 
#         continue
#     else:
#         print(x)

# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#               innerloop:

# rows = int(input("Enter the # of rows:"))
# columns = int(input("Enter the # of colums: "))
# symbol = input("Enter a symbol to use ")

# for x in range(rows):
#   for y in range(columns):
#     print(symbol, end="")   
#     print()   



# for x in range(1,11):
#     print(x, end=" ")


# import time 

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60 % 60)
#     hours = int(x / 3600 % 24)
#     print(f"{hours}:{minutes:2}:{seconds:2}")
#     time.sleep(1)


# print("TIME'S UP !")










# Colletion = single "variable" used to store multiple values
# List =  [] ordered and changeable. Duplicates OK
# Set =   {} unordered and imutable, but Add/Remove OK , NO duplicates 
# Tuple = () ordrered and unchangeable, Duplicates OK, FASTER


# fruits = ["apple","orange","banana","coconut"]

# print(fruits[::-2])


    # print(dir(fruits))
    # print(help(fruits))
    # print(len(fruits))
    # print("pineapple" in fruits )


    # fruits[0] = "pineapple"
    # print(fruits[0])
# fruits.append("pineapple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# print(fruits.index("coconut"))
# print(fruits)
# print(fruits.count("pineapple" in fruits))

# print(fruits[0])

# for fruit in fruits:
    # print(fruit)







#Shopping cart program 

# foods = []
# prices = []
# total = 0 

# while True:
#     # food = input("Enter a foood to buy (q to quit): ")
#     food = input("Enter a foood of a {food}: ")
#     foods.append(food)
#     if food == "q":
#         break
#     else:
#         price = float(input("Enter the price of the {food}: $"))
#         price = input(food)
#         prices.append(price)  

#         print("--------YOUR CART-------------")
#         print("Food, ")



# fruits = ["apple", "orange", "banana","coconut"]
# vegetables = ["celebry", "carrots","potatoes"] 
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[1][1])


# groceries = ({"apple", "orange", "banana", "coconut"},
# {"celery","carrots","potatoes"},
# {"chicken","fish", "turkey"})          

# for collection in groceries:
#     for food in collection:
#         print(food, end =" ")
#         print()

# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*", 0,"#"))

# for row in num_pad:
#     for num in row:
#         print(num, end= " ")
#         print()






# Python quiz game 

# questions = (
#     "How many elements are in the periodic table?:",
#     "Which animal lays the largest eggs?:",
#     "What is the most abundant gas in Earth's atmosphere?:",
#     "How many bones are in the body?:",
#     "Which planet in the solar system is the hottest?:"
# )

# options = (
#     ("A. 116", "B. 117", "C. 118", "D. 119"),
#     ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#     ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#     ("A. 206", "B. 207", "C. 208", "D. 209"),
#     ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
# )

# correct_answers = ("C", "D", "A", "A", "B")

# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("---------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
    
#     guess = input("Enter your answer (A, B, C, or D): ").upper()
#     guesses.append(guess)
    
#     if guess == correct_answers[question_num]:
#         print("Correct")
#         score += 1
#     else:
#         print("Incorrect")
    
#     question_num += 1

# print("---------------------")
# print("Game Over")
# print(f"Your score is: {score}/{len(questions)}")

# print("correct_answers", end="" )
# for question_num, correct_answer in enumerate(correct_answers):
#     print(f"Question {question_num + 1}: {correct_answer}")
#     print("guesses", end="")
#     print("guesses", end=" ")
#     score = int(score / len(questions) *100) 
#     print(f"Your score is : {score}")    

# dictionsry = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# capitals = {"Brasil":"Brasília",
#         "India": "New Delhi",
#         "China":"Beijing",
#         "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Brasil"))
# print(capitals.get("India"))
# print(capitals.get("China"))
# print(capitals.get("Russia"))

# if capitals.get("Brasil"):
#     print("That capital exits")
# else:
#     print("That capital doesn't exist")

# if capitals.get("India"):
#     print("That capital exits")
# else:
#     print("That capital doesn't exist")

# if capitals.get("China"):
#     print("That capital exits")
# else:
#     print("That capital doesn't exist")

# if capitals.get("Russia"):
#     print("That capital exits")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Brasil": "Brasília"})
# capitals.update({"Russia": "Moscow"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# print(capitals)


# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)













# Concession stand Program


# menu = {"Pizza": 3.00,
#         "nachos": 4.50,
#         "hamburguer":10.50,
#         "popcorn" :7.50,
#         "Fries": 5.00,
#         "Pretzael":8.95,
#         "Soda": 3.00,
#         "Lemonade": 4.85}

# cart = []
# total = 0

# for key, value in menu.items():
#     print(f"{key}: ${value:.2f}")
#     while True:
#         choice = input("Do you want to buy this item? (yes/no):")
#         if choice.lower() == "yes":
#             cart.append(key)
#             total += value
#             break
#         elif choice.lower() == "no":
#             break
#         else:
#             print("Invalid choice. Please enter yes or no.")           

# Import random

# import random



# low = 1 
# high = 1000
# options = ("Rock", "paper", "Scissors")
# cards = ["2", "3", "4", "5", "6","7", "8", "9","10", "J", "Q", "K","A"]


# number = random.randint(low, high)
# number = random.random()


# number = random.randint(1, 13)
# random.shuffle(cards)

# print(cards)


# low = 1
# high = 100
# guesses = 0
# number = random.randint(low, high)


# while True:
#     guess = int(input(f"Enter a number between ({low} - {high}):"))   
#     guesses += 1 

#     if guess < number :
#         print(f"{guess} too low!")
#     elif guess > number :
#         print(f"{guess} too high")
#     else:
#         print(f"Yay! You found the number in {guesses} guesses")
        # break
    # print(f"Yay! You found the number in {guesses} guesses")


# lowest_num = 1
# highest_num = 1000
# answer = random.randint(lowest_num, highest_num )
# guesses = 0 
# is_running = True


# print(answer)

# Python number guessing game 

# import random

# lowest_num = 1
# highest_num = 1000
# answer = random.randint(lowest_num, highest_num)
# guesses = 0 
# is_running = True

# print("Python Number Guessing Game")
# print("-------------------------------")
# print(f"Select a number between {lowest_num} and {highest_num}")
# print("-------------------------------")

# while is_running:
#     user_guess = input("Enter your guess: ")
#     guesses += 1
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#         if user_guess < answer:
#             print(f"{user_guess} is too low")
#         elif user_guess > answer:
#             print(f"{user_guess} is too high")
#         else:
#             print(f"Yay! You found the number in {guesses} guesses")
#             is_running = False
#     else:
#         print("Invalid input. Please enter a number")
#         print("-------------------------------")
#         print("Game Over.")
#         print("-------------------------------")





# import random 

# options = ("Rock", "Paper", "Scissors")
# player = None
# computer = random.choice(options)

# while player not in options:
#     player = input("Enter Rock, Paper, or Scissors: ").capitalize()
#     if player not in options:
#         print("Invalid input. Please enter Rock, Paper, or Scissors.")

# print(f"Player: {player}")
# print(f"Computer: {computer}")

# if player == computer:
#     print(f"Both players selected {player}. It's a tie!")
# elif player == "Rock":
#     if computer == "Scissors":
#         print("Rock smashes scissors! Player wins!")
#     else:
#         print("Paper covers rock! Computer wins!")
# elif player == "Paper":
#     if computer == "Rock":
#         print("Paper covers rock! Player wins!")
#     else:
#         print("Scissors cuts paper! Computer wins!")
# elif player == "Scissors":
#     if computer == "Paper":
#         print("Scissors cuts paper! Player wins!")
#     else:
#         print("Rock smashes scissors! Computer wins!")
#         print("-------------------------------")
#         print("Game Over.")
#         print("-------------------------------")

# import random
# import string

# chars = string.punctuation + string.digits + string.ascii_letters 
# chars = list(chars)
# key = chars.copy()
# Key = list(chars)


# random.shuffle(key)

# print (f"chars: {chars}")
# print (f"Key {key}")

# ciapher_text  = input("Enter a message to encrypt: ")
# plain_text = ""
# for letter in plain_text:
#     index = chars.index(letter)
#     ciapher_text += key[index]
#     print(f"Original Message: {ciapher_text}")
#     print(f"encrypted message: {plain_text}") 
# def encrypt(text):
#     encrypted = ""  
#     for i in range(len(text)):
#         encrypted += key[chars.index(text[i])]
#         return encrypted
#     def decrypt(encrypted):
#         decrypted = ""
#         for i in range(len(encrypted)):
#             decrypted += chars[key.index(encrypted[i])]
#             return decrypted
#         print("-------------------------------")        
# print(chars)

# function = A block of reusable code 
#            Place () after the functon name to invoke it


# def happy_birthday(name, age):
#     print(f"Happy birthday to you, {name}!")
#     print(f"You are {age} years old! ")
#     print("Happy bithday to you! ")
#     print() 

# happy_birthday("José", 19)    
# happy_birthday("Aldry",43)    
# happy_birthday("Adna",39)    
# happy_birthday("Maria", 84)    
# happy_birthday("Ted", 8)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}: ")
#     print(f"Your bill of ${amount} is due: {due_date}")
#     print("Thank you for your payment!")
#     print()

# display_invoice("José Tiago", 844.00, "27/09")


# return = startment used to end a fuction 
#          and send a result back to the caller 

# def add(x,y):
#     f = x + y 
#     return f

# def subtract(x,y):
#     f = x-y
#     return f


# def multiply(x,y):
#     f = x*y
#     return f

# def divide(x, y):
#     if y == 0:
#         return
#     f = x / y
#     return f

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))


# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first +" "+ last 

# full_name = create_name("José", "Tiago")
# print(full_name)

#  default arguments = A defaut value for certain parameters 
#                      defaut is used when that argument is omitted
#                      make your functions more flexible,reduces # Of arguements 
#                      1. positional, 2. DEFAULT, 3. keyword, 4. Arbitrary
 
# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1-discount) * (1 + tax)

# print(net_price(500,0.05))
# print(net_price(500,0.9))
# print(net_price(500, 0.4 , 0))
# print(net_price(500, 0.6, 0))

# Exercise

# import time

# def count(start, end):
#     for x in range(start, end):
#         print(x)
#         time.sleep(1)
#     print("DONE !")

# count(0, 10)

#  keyword arguments = an arhuments preceded by an identifier
#                      helps with readability
#                      order of arguments doesn't matter
#                   1.positional 2.default 3.keyword 4.arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello(greeting= "Hello", title = "MR.", first="José", last ="Tiago")

# for x in range(1, 11):
#     print(x, end = "  ")


# print("1", "2", "3", "4","5", sep="-") 

# def get_phone(country, area, first, last):
#     return f"{country}--{area}--{first}--{last}"

# phone_num = get_phone(country=1, area=123, first=456, last=7890)
# print(phone_num)


# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#           * unpacking operator 
#           1. positional 2. default 3. keyword 4.ARBITRARY

# def add(a, b):
#     return a + b
# print(add(1,2,3))


# def add(*args):
#     total = 0 
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5))

# ------------------------------------------
# ------------------------------------------
# ******************************************
# Exemple 3

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4,8,9,10,17))

# def display_name(*args):
#     for name in args:
#         print(name, end = " ")
# display_name("Aldry","Tiago","Adna","Davi","Ted")
# -----------------------------------------------------
# -----------------------------------------------------
# ******************************************************
# Exemple 3
# -----------------------------------------------------
# ------------------------------------------------------
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_address(street= "638 Rua Pedro Rosa Da Silva",
#                city = "Cidade = Extrema",
#                state= "Minas Gerais",
#                country = "Brasil" )


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()  
#     if "apt" in kwargs:
#         print(f"{kwargs.get('streat')} {kwargs.get('apt')}")
#         print(f"{kwargs.get('city')}")
#         print(f"{kwargs.get('state')} {kwargs.get('zip')}")
#         print(f"{kwargs.get('country')}")
#     else:
#         print(f"{kwargs.get('streat')}")
#         print(f"{kwargs.get('city')}")
#         print(f"{kwargs.get('state')} {kwargs.get('zip')}")
#         print(f"{kwargs.get('country')}")
# shipping_label("Dr", "José", "Tiago", 
#                 streat = "Estrada Municipal Pedro Rosa Silva ",
#                 apt = "#100",
#                 city = "Extrema",
#                 state = "Minas Gerais",
#                 country = "Brasil",
#                 zip_code = "35640-000")

  # for value in kwargs.values():
    #     print(value, end="  ")
    #     print()

# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop 

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)
#     # -----------------------------------------------------

# for number in reversed(numbers):
#     print(number, end=" ")

# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
#     print(fruit)
# -----------------------------------------------------

# name = "José Tiago"
# print("---------------------------------------------------")
# for character in name:
#     print(character, end =" ")

# my_dictionary = {"A": 1, "B": 2, "C": 3}

# for value in my_dictionary:
#     print(value, end="")
#     print (my_dictionary[value], end = " ")

# Module = A file contain code you to includ in yout program 
#          Use 'import' to include a module {bult-in or your own}
#          Useful to a break up a large program resauble separate files 
# ------------------------------------------------------------

# THIS IS AN EXAMPLE 1

# import math
# print(help("modules"))

# import math 
# print(math.pi)
# ------------------------------------------------------------
# import math as m 

# print(m.pi)
#-------------------------------------------------------------

# THIS IS AN EXAMPLE 2

# from math import pi

# print(pi)

#-------------------------------------------------------------

# THIS IS AN EXAMPLE 3

# from math import e 

# a, b, c, d= 1,2,3,4

# print(e**a)
# print(e**a)
# print(e**a)
# print(e**a)
# print(e**e)

# ------------------------------------------------------------

# THIS IS AN EXAMPLE 4 AND ITS NAME IS A CREATED MODULE
# import  math

# pi = 3.14159

# def square(x):
#     return x**2
# # ------------------------------------------------------------
# def cube(x):
#     return x**3

# #---------------------------------------------------------------

# def circumference(radius):
#     return 2 * pi * radius

# # --------------------------------------------------------------

# def area(radius):
#     return pi * radius ** 2

# # --------------------------------------------------------------

# result = square(3)
# print(result)
# # --------------------------------------------------------------
# result = cube(3)
# print(result)
# # --------------------------------------------------------------
# result = circumference(3)
# print(result)
# # --------------------------------------------------------------
# result = area(3)
# print(result)
# #--------------------------------------------------------------


#  Variable scope = where a varieble is visible and acessible
# Scape resolution = (LEGB) Local -> Enclosed -> Built-in 



# def func1():
#     x = 1
#     print(x)
# def func2():
#     x = 2
#     print(x)

# func1()
# func2()      
# 
# def func1():
#     print(x)
# def func2():
#     print(x)

# x = 3
# func1()
# func2()

# Example 3 

# from math import e
# import random

# def func1():
#     e = 2.71828
#     print(e)

# func1()
   

# Membership operators = used to text whenther a value or variable is found a sequence

# word = "APPLE"

# letter = input("Guess a letter in the secret word:")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"There is no {letter}")

# word = "APPLE"

# letter = input("Guess a letter the secret word")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")


# students =  {"Bruno", "Tiago", "Felipe", "Malcom"}

# student = input("Enter the name of a student:")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# grades = {"Malcom": "A",
#           "Tiago": "B",
#           "Bruno": "C",
#           "Felipe":"D"}

# student = input("Enter the name of a student:")

# if student in grades:
#     print(f"{student} has a grande of{grades[student]} ")
# else:
#     print(f"{student} was a student")

# email = "moraestiago@gmail.com"

# if "@" in email and ".":
#     print("This is a valid email")
# else:
#     print("This is not a valid email")
#     print("The program has finished")

# email = "moraestiago@gmail.com"

# panssword = "123456"

# email = input("Enter your email: ")

# panssword = input("Enter your password:")

# if panssword == "123456":
#     print("You have entered the correct password")
# else:
#     print("You have entered the incorrect password")
    

# if "@" in email and ".":
#     print("This is a valid email")
# else:
#     print("This is not a valid email")
#     print("The program has finished")
    
#  List comprehensiom = A consecise to create list in Python
#                    Compact and easier to read than traditional loops
#                    [expression for value in iterable if condition]

# doubles = []

# for x in range(1,11):
#     doubles.append(x*2)
# print(doubles)

# doubles = [x * 2   for x in range(1,11)]

# print(doubles)


# fruits = ["Apple", "Orange", "Banana", "Coconut"]

# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6, -7, 8]

# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if  num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]


# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]

# passing_grades = [grades for grades in grades if grades >= 60]

# print(passing_grades)

#  Match-Case stratment (switch): An alternative to using many 'elif' statements 
#   Execute some code if a value matches a 'case'
#  Benefits: Cleaner and syntax is more readadle

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Wednesday"
#         case 4:
#             return  "It is Thursday"
#         case 5:
#             return "It is Friday"
#         case 6:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"
# print(day_of_week(1)) 
# print(day_of_week(2))
# print(day_of_week(3))
# print(day_of_week(4))
# print(day_of_week(5))
# print(day_of_week(6))     

# def day_of_week(day):
#         match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Wednesday"
#         case 4:
#             return "It is Thursday"
#         case 5:
#             return "It is Friday"
#         case 6:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"

# print(day_of_week(1)) 
# print(day_of_week(2))
# print(day_of_week(3))
# print(day_of_week(4))
# print(day_of_week(5))
# print(day_of_week(6))


#  if__name__ === "__ main__": (This script van be imported or run standalone )
#                            Fuctions and classes in this can be reused 
#                            Without the main block of code executing

# def favorite_food(food):
#     print(f"Your favorite food is {food}")

# def main():
#      print("This is script")
#      favorite_food("Hamburguer")
#      print("This is the end of the script")

# if __name__ == '__main__':
#     main()



# def favorite_drink(drink):
#     print(f"Your favorite drink is {drink}")

# def main():
#     print("This is script2")
#     favorite_drink("Coca-Cola")
#     print("This is the end of the script2")

# if __name__ == '__main__':
#     main()


#  Python Credit carf valiadar program 

# 1. Remove any '-' or ' '
# 2. Add all digits in the old places from right to left 
# 3. Double every second digit from right to left.
#                (If result is a two-digit number, 
#                 add the two-digit number together to get a single digit. )
# 4. Sum the totals of totals of steps 2 & 3
# 5. If sum is divisible by  10, the credit card # is valid 

# sum_odd_digits = 0
# sum_even_digits = 0
# total = 0
# card_number = "123456789" 
# Step 1 

# card_number = input("Enter a credit card #")
# card_number = card_number.replace("-", "")
# card_number = card_number.replace("-", "")
# card_number = card_number[::-1]


#  Step 2

# for x in card_number [::2]:
#     sum_odd_digits += int(x)
# print(sum_odd_digits)
    # sum_odd_digits = sum_odd_digits

# Step 3

# for x in card_number[::-1]:
#     x = int(x) * 2
#     if x > 10:
#         sum_even_digits + (1 + (x % 10))
#         sum_even_digits + (x // 10)
#     else:
#         sum_even_digits += x
#         print(sum_even_digits)

# Step 4 
# total = sum_odd_digits + sum_odd_digits

# Step 5 
# if total % 10 == 0 :
#     print("Credit card # is valid")
# else:
#     print("Credit card # is not valid")


# Python Banking Program 
# def show_balance():
#     print(f"Your balance is ${balance:.2f}")

# def deposit():
#     amount = float(input("Enter the amount to deposit: $"))
#     return amount

# def withdraw():
#     amount = float(input("Enter the amount to withdraw: $"))
#     if amount > balance:
#         print("Insufficient funds")
#         return 0
#     else:
#         return amount

# balance = 0
# is_running = True

# while is_running:
#     print("1. Show Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
#     choice = input("Enter your choice (1-4): ")
   
#     if choice == "1":
#         show_balance()
#     elif choice == "2":
#         balance += deposit()
#     elif choice == "3":
#         withdrawal_amount = withdraw()
#         if withdrawal_amount > 0:
#             balance -= withdrawal_amount
#             print(f"Withdrew ${withdrawal_amount:.2f}")
#     elif choice == "4":
#         is_running = False
#     else:
#         print("Invalid choice. Please try again.")


# Python Sloat Machine 

# def spin_row():
#     symbols = ['🥕🥔🌽🥞🍒']
#     return [random.choice(symbols)for _ in range(3)]
# def print_row():
#     pass

# def get_payout(row,bet):
#     if row [0] == row [1] == row[2]:
#         if row[0] == '🥕':
#             return bet * 3
#         elif row[0] == '🥔':
#             return bet * 4
#         elif row[0] == '🌽':
#             return bet * 5
#         elif row[0] == '🥞':
#             return bet * 10
#         elif row[0] == '🍒':
#             return bet * 20
# def main():
#     balace = 100
#     print("***********************")
#     print("Welcome to Python Slots")
#     print("Symbols:🥕🥔🌽🥞🍒")
#     print("***********************")
#     print("***********************")

#     while balace > 0:
#         print(f"Currets balace: ${balace}")

#         bet = input("Place your bet amount: ")
        
#         if not bet.isdigit():
#             print("Please enter a your a valid number ")
#             continue

#         bet = int(bet)

#         if bet > balace:
#             print("You don't have enough money to place that bet")
#             continue

#         if bet <= 0:
#             print("Please enter a valid bet amount")
#             continue

#         balace -= bet

#         ro w = spin_row()
#         print(row)
    
# if __name__ == '__main__':
#     main()



# reponse = (input(f"Do you like hamburgers and Hot dog ? (yes/no) : "))
# if reponse.lower() == "yes":
#     print("Great I love  hambugers and hot dogs are delicius ")
# elif reponse.lower() == "no":
#     print("That's okay, everyone has different tastes! ")
# else:
#     print("Sorry =, I didn't understand your response.")
#     print("Thanks for playing!")




# object = A "bundle" of related atributes (variables) and methods (functions)
#           Ex: phone , cup , book
#           You need = " class" to create many objects
#  class = (blueprint) used to design the stucture and layout of an object

# class Car:
#     def __init__(self, model,year, color,for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

# car1 = Car("FERRARI 125 S" ,1947,"Red",False) 
# car2 = Car("Corvette", 2025, "Black", True) 

# print(car1.model)
# print(car1.color)
# print(car1.year)
# print(car1.for_sale)
# print(car2.model)
# print(car2.color)
# print(car2.year)
# print(car2.for_sale)
