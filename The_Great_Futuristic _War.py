import random

class character:
  def __init__(self,name,weapon,hp):
    self.name=name
    self.weapon = weapon
    self.hp = hp
  def attack(self,enemy):
    damage = self.weapon.damage
    enemy.hp -= damage
    print(f"{self.name} attacks {enemy.name} with {self.weapon.name} causing {damage} damage.")
    print(f"{enemy.name} has {enemy.hp} HP left.")

class Enemy:
    def __init__(self, name, damage, hp):
        self.name = name
        self.hp = hp
        self.damage = damage
    

def attack(self,character):
    character.hp -= self.damage
    print(f"{self.name} attacks causing{self.damage} causing {self.damage} damage ")
    print(f"{character.name} has {character.hp} HP left.")
class weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

furistic_katana = weapon("Futuristic Laser Katana", random.randint(15,20))
energy_blaster = weapon("Energy Blaster", random.randint(25,35))
plasma_sword = weapon("Plasma Sword",random.randint(20,40))

def print_welcome():
    print("Welcome to the Great Futuristic War Game!")
    print("You are the commander of the Galactic Empire.")
    print("Your goal is to defend the entire galaxy.")
    print("You will be given a series of challenges to overcome.")
    print("You will have to make strategic decisions to win the game.")
    print("Let's start the game!")
def choose_character():
    print("Choose your character:")
    print("1. Futuristic Galactic Samurai")
    print("2. Android Space")
    print("3. Alien Warrior")
    choice = input("Enter your choice: ")
    if choice == "1":
        return "Futuristic Galactic Samurai"
    elif choice == "2":
        return "Android Space"
    elif choice == "3":
        return "Alien Warrior"
    else:
        print("Invalid choice. Please choose again.")
        return choose_character()
def Character_Class_Weapons():
    print("Choose your character's class and weapon:")
    print("1. Futuristic Galactic Samurai - Futuristic laser katana")
    print("2. Android Space - Energy Blaster")
    print("3. Alien Warrior - Plasma Sword")
    choice = input("Enter your choice: ")
    if choice == "1":
        return "Futuristic Galactic Samurai - Futuristic laser katana"
    elif choice == "2":
        return "Android Space - Energy Blaster"
    elif choice == "3":
        return "Alien Warrior - Plasma Sword"
    else:
        print("Invalid choice. Please choose again.")
def choose_planet():
    print("Choose a planet to defend:") 
    print("1. Earth")
    print("2. Saturn Stars")    
    print("3. Urano ")
    choice = input("Enter your choice: ")
    if choice == "1":
        return "Earth"
    elif choice == "2":
        return "Saturn Stars"
    elif choice == "3":
        return "Urano "
    else:
        print("Invalid choice. Please choose again.")
        return choose_planet()
    
def choose_enemy():
    print("Choose an enemy to fight:")
    print("Invasion of humans dressed in astronautical suits possessed by ghosts")
    print("Invasion of six-armed werewolf aliens from Mars")
    print("Invasion of giant, mutated, space-dwelling spiders")
    choice = input("Enter your choice: ")
    if choice == "1":
        return "Invasion of humans dressed in astronautical suits possessed by ghosts",110,15
    elif choice == "2":
        return "Invasion of six-armed werewolf aliens from Mars",160,10
    elif choice == "3":
        return "Invasion of giant, mutated, space-dwelling spiders",100,30
    else:
        print("Invalid choice. Please choose again.")
        return choose_enemy()
def battle(character,enemy):
    print(f"The battle begins! {character.name} vs {enemy.name}")
    while character.hp > 0 and enemy.hp > 0:
        character.attack(enemy)
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated")
        break
    enemy.attack(character)
    if character.hp <= 0:
        print(f"{character.name} has been defeated!")
        return False 
    return True
def game():
    print("Welcome to the game!")
    print("You are a brave space warrior, and you have been tasked with defending the galaxy from")
    print("an alien invasion.")
    print_welcome()
    character = choose_character()
    planet = choose_planet()
    enemy = choose_enemy()
    print(f"You are a {character} defending {planet} against {enemy}")
    print("You have been equipped with a laser gun and a spaceship.")
    print("You are ready to defend the galaxy. Good luck!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        game()
    else:
        print("Thanks for playing!")
game()