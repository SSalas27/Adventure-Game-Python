import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(): 
    print_pause("You find yourself in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked werewolf is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def house(items):
    print_pause("You find yourself in front of the house and you knock on the door.")
    print_pause("When the door opens, you see a big, mean werewolf about to attack you.")
    
    if "sword" in items: 
        print_pause("Luckliy you have your magical sword to fight the werewolf."
                    "You victoriously defeat the werewolf.")
    else:
        print_pause("Oh no! The werewolf is about to attack you and your old dagger will just not do.")
        print_pause("The werewolf has defeated you.")
    valid_input(items)

def cave(items):
    print_pause("You cautiously head into the cave.")
    print_pause("You realize it is dark and small.")

    if "sword" in items: 
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("Your eye catches a glint of metal behind a rock."
                    "As you approach it, you realize it is a magical sword."
                    "You leave your silly old dagger and take the sword with you.")
        items.append("sword")
    print_pause ("You walk back out to the field")
    valid_input(items)

def valid_input(items): 
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2)")

    choice = input ("Enter 1 to knock on the door of the house.\n"
                    "Enter 2 to peer into the cave.\n")

    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)

def play_game():
    items = []
    intro()
    valid_input(items)

play_game()











    

 
