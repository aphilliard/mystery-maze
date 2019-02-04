import random
import sys
import os

entered_from = "n"
game_won = False

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def display_intro():
    cls()
    print("You are lost in the ever-changing maze of Mister Mystic: Master of Magic and Mystery!\n")
    print("The only way out is to find the hidden treasure chest! But beware, intrepid intruder!\n")
    print("There are many foul and nasty things left behind by his previous playthings...")
    print()
    print()

def encounter_chance():
    item_list = ["treasure chest", "lump of coal", "dead cat", "box of stale donuts", "loaf of moldy bread", "used hanky", "foul stench", "green globule", "flat tire"]
    disgust_word_list = ["Gross!", "Nasty!", "Ew!", "Foul!"]
    chance_encounter = random.randint(1,3)
    found_item = random.choice(item_list)
    if chance_encounter == 3:
        print(f"You found a {found_item}.")
        if found_item == "treasure chest":
            print("You won the game!")
            raise SystemExit
        else:
            print(random.choice(disgust_word_list))
    else:
        print("The room is empty.")

def create_exit_doors():
    exit_doors_list = ["n", "e", "s", "w"]
    random.shuffle(exit_doors_list)
    global entered_from
    if entered_from == "n":
        old_from = "s"
    elif entered_from == "w":
        old_from = "e"
    elif entered_from == "e":
        old_from = "w"
    else:
        old_from = "n"

    number_of_exits = random.randint(1,4)
    while number_of_exits <= len(exit_doors_list):
        exit_doors_list.remove(random.choice(exit_doors_list))
        
    if old_from not in exit_doors_list:
        exit_doors_list.append(old_from)
    print(exit_doors_list)
    
    player_choice = input("Go where? 'q' to QUIT\n")
    while player_choice not in exit_doors_list and player_choice != "q":
        print("Invalid choice. These are your choices:")
        print(exit_doors_list)
        player_choice = input("Go where? 'q' to QUIT\n")

    if player_choice == "q":
        raise SystemExit       
    else:
        entered_from = player_choice        
    return exit_doors_list

def main_loop():
    display_intro()
    while not game_won:
        create_exit_doors()
        print(f"You move {entered_from}.")
        encounter_chance()

main_loop()

