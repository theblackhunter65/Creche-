def print_welcome():
   print("Welcome ladies and Gentleman boys and Girls ")
   print("This is a simple game War-Dimensions")
   print("Well let's play game")
def choose_character():
    print("Choose your character:")
    print("1 - Warrior-Future")
    print("2 -Warrior-Lizard")
    print("3 - Alien-Warrior")
    choice = input("Only these classes and one character can: ")

    if choice == "1":
      print("You chose Future-Warrior")
      return"Future-Warrior",76
    elif choice == "2":
       print("You chose Warrior-Lizard")
       return "Warrior-Lizard",75
    elif choice == "3":
       print("You chose Alien-Warrior")
       return "Alien-Warrior",78
    else:
     print("Invalid choice")
     return None, 0
def choose_weapon():   
 print("And now choose your weapon")
 print("1 - Alien Sword")
 print("2 - Claws Lizard")
 print("3 -Laser Gun")
 weapon_choice=input("Only these weapons and one weapon can:")
 if weapon_choice == "1":
    print("You chose Alien Sword")
    return ("Alien Sword") , 90 
 elif weapon_choice == "2":
    print("You chose Claws Lizard")
    return ("Claws Lizard"), 45
 elif  weapon_choice == "3":
    print("You chose Laser Gun")
    return ("Laser Gun"), 100
 else:
    print("Invalid choice")
    return None, 0
def choose_clothes():
  print("And now choose clothes")
  print("1 - Future Armor")
  print("2 - The skin Warrior-Lizard")
  print("3 - The skin Alien Warrior")
  clothes_choice=input("Only these clothes and one clothes can:")
  if clothes_choice == "1":
    print("You chose Future Armor")
    return ("Future Armor"), 40
  elif clothes_choice == "2":
    print("You chose The skin Warrior-Lizard")
    return ("The Skin Warrior-Lizard"), 38
  elif clothes_choice == "3":
    print("You chose The skin Alien Warrior")
    return ("The Skin Alien Warrior"), 39
  else:
    print("Invalid choice")
    return None, 0
def choose_vilain():
   print("And now choose villains:")
   print("1 - The Future Robot")
   print("2 - The Wolf King")
   print("3 - The Human Queen")
   villain_choice = input("Only these vilans and one villain can:")
   if villain_choice == "1":
       print("You chose The Future Robot")
       return ("The Future Robot"), 115
   elif villain_choice == "2":
    print("You chose The Wolf King")
    return ("The Wolf King"), 250
   elif villain_choice == "3":
    print("You chose The Human Queen")
    return ("The Human Queen"), 100
   else:
    print("Invalid Choice")
    return None, 0
   
def start_game():
  print_welcome

  character, character_power = choose_character()
  weapon, weapon_power = choose_weapon()
  clothes, clothes_power = choose_clothes()
  villain,villain_power = choose_vilain()

  total_power = character_power + weapon_power + clothes_power
  print(f"Total Power:{total_power}")
  print(f"Villain Power: {villain_power}")
  if total_power > villain_power:
    print("You Win!")
  else:
    print("Game Over")
start_game()
    