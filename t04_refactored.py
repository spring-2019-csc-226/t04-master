######################################################################
# Author: The Spring 2019 226 Class!
#
# Assignment: T04: Adventure in Gitland
#
# Purpose: To recreate a choose-your-own-adventure style game
# by refactoring T01.
#
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
#
# This new version will take advantage of functions, as well as
# demonstrate the value of git as a tool for collaborating.
######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
#
######################################################################
import random
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False


def start_story():
    """
    Introduction text for the story. Don't modify this function.
    :return: the user's name, captured from user input
    """
    global username
    username = input("What do they call you, unworthy adversary? ")
    print()
    print()
    print("Welcome, " + username + ", to the labyrinth.")
    sleep(delay)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(delay)
    return username


def end_story(username):
    """
    This is the ending to the story. Don't modify this function, either.
    :param user: the user's name
    :return: None
    """
    print("Congratulations, " + username + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay*5)
    print("Now go play again!")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead
    :param dead: A boolean value where false let's the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()

###################################################################################


def sample_adventure():
    """
    Original adventure text given as an example. Leave it alone as well.
    :return: None
    """
    global dead             # You'll need this to be able to modify the dead variable
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(delay*2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)


#########################################################################################################
# Audrey, Lesley, and Anya
# Refactored by Team 1:                 #TODO Team 1 names here
# Google doc link:                      #TODO Team 1 Google doc link here
def team_1_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Darian and Alex
# Refactored by Team 2:                 #TODO Team 2 names here
# Google doc link:                      #TODO Team 2 Google doc link here
def team_2_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Evan, Hila, and Megan
# Refactored by Team 3:                 #TODO Team 3 names here
# Google doc link:                      #TODO Team 3 Google doc link here
def team_3_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Irfan and David
# Refactored by Team 4:                 #TODO Team 4 names here
# Google doc link:                      #TODO Team 4 Google doc link here
def team_4_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Jalen and Tabias
# Refactored by Team 5:                 #TODO Team 5 names here
# Google doc link:                      #TODO Team 5 Google doc link here
def team_5_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Karmadri and Lisandro
# Refactored by Team 6:                 #TODO Team 6 names here
# Google doc link:                      #TODO Team 6 Google doc link here
def team_6_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Kenzie and Caleb
# Refactored by Team 7:                 #TODO Team 7 names here
# Google doc link:                      #TODO Team 7 Google doc link here
def team_7_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Liberty and Joseph
# Refactored by Team 8:                 #TODO Team 8 names here
# Google doc link:                      #TODO Team 8 Google doc link here
def team_8_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Mahmoud and Shageldi
# Refactored by Team 9:                 #TODO Team 9 names here
# Google doc link:                      #TODO Team 9 Google doc link here
def team_9_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Nicole and Eleni
# Refactored by Team 10:                 #TODO Team 10 names here
# Google doc link:                       #TODO Team 10 Google doc link here
def team_10_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Roberto and David
# Refactored by Team 11:                 #TODO Team 11 names here
# Google doc link:                       #TODO Team 11 Google doc link here
def team_11_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Sandesh
# Refactored by Team 12:                 #TODO Team 12 names here
# Google doc link:                       #TODO Team 12 Google doc link here
def team_12_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Johnathan and Will
# Refactored by Team 13:                 #TODO Team 13 names here
# Google doc link:                       #TODO Team 13 Google doc link here
def team_13_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Nmasichi, Kabelo, and Christian
# Refactored by Team 14:                 #TODO Team 14 names here
# Google doc link:                       #TODO Team 14 Google doc link here
def team_14_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Trent and Dustin
# Refactored by Team 15:                 #TODO Team 15 names here
# Google doc link:                       #TODO Team 15 Google doc link here
def team_15_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Tristan and Azah
# Refactored by Team 16:                 #TODO Team 16 names here
# Google doc link:                       #TODO Team 16 Google doc link here
def team_16_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Ben and Luis
# Refactored by Team 17:                 #TODO Team 17 names here
# Google doc link:                       #TODO Team 17 Google doc link here
def team_17_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Minh and Taran
# Refactored by Team 18: Luis and Tabias
# Google doc link:
# https://docs.google.com/document/d/1RdhX6OoMjEDKT3oPqSmkpZwPORe1nIQC3vnslmjSrCM/edit?ts=5c58b1af#heading=h.f6tumop9n7at
def team_18_adv():
    # prompts for a weapon choice
    print("")
    print("You  come across a dungeon armory.")
    print("The door behinds you lock behinds you as the one in front of you opens. \n")
    print("What weapon would you like to use from the armory?")
    print("1. Sword")
    print("2. Staff")
    print("3. Bow and Arrow")
    print("4. Bare hands")
    choice_1 = input()
    if choice_1 == "1" or "sword" in choice_1.lower():
        print("You got an iron sword!!")
        print("You see yourself as a knight")
    elif choice_1 == "2" or "staff" in choice_1.lower():
        print("You got a wooden staff")
        print("You feel dark magic around you")
    elif choice_1 == "3" or "bow and arrow" in choice_1.lower():
        print("You got a bow and 20 arrows")
        print("You feel weird carrying the bow?")
    elif choice_1 == "4" or "bare hands" in choice_1.lower():
        print("You feel weaker than before")
    else:
        print("You are kidding me, right? You want that?")
        print("The story teller killed you!!!")
        dead = True
        kill_if_dead(dead)

    choice_2 = input("""You entered the dungeon\nThere are 2 doors
One to the left and one to the right\nWhere will you go?""")
    # tracks if the player has run through this before
    attempt = 0
    while attempt == 0 or 1:
        # fight against the dark wizard
        if "left" in choice_2.lower():
            print("You encounter the dark wizard")
            print("What are you going to do?")
            print("1. Hit\n2. Technique")
            if attempt == 0:
                print("3. Run")
            fight = input()
            if fight == '1' or "hit" in fight.lower():
                print("He threw a thunderbolt")
                print("You fried a bit")
                if choice_1 == '1' or "sword" in choice_1.lower():
                    print("You swing your sword. Cutting him in half")
                elif choice_1 == '2' or "staff" in choice_1.lower():
                    print("You beat him continuously with your staff")
                elif choice_1 == '3'or "bow and arrow" in choice_1.lower():
                    print("You shoot an arrow straight into his heart")
                    print("Sadly you aren't cupid")
                    sleep(delay)
                elif choice_1 == '4' or "bare hands" in choice_1.lower():
                    print("You punch him to death")
                    print("Who feels weak now?!")
                print("He is dead")
                print("A chest appears in front of you")
                print("You open it\nGold coming out\nYou're rich!")
                # code that ends the run by killing the wizard
                # print("You escape the dungeon and live a happily ever after.\nYou died because of old age.")
                # dead = True
                # kill_if_dead(dead)
            elif fight == '2' or "technique" in fight.lower():
                print("You perform your move in front of him\n He gets mad")
                print("He uses his staff to whack your head")
                dead = True
                kill_if_dead(dead)
            elif attempt == 0 and fight == "3" or "run" in fight.lower():
                print("You run back to the other room")
                attempt + 1
                choice_2 = "right"
            else:
                print("You are kidding me, right? You want that?")
                print("The story teller killed you!!!")
                dead = True
                kill_if_dead(dead)
        # encounter dragon woman
        elif "right" in choice_2.lower():
            print("You see a beautiful woman sitting on a bed")
            print("1. Hit\n2. Technique")
            if attempt == 0:
                print("3. Run")
            fight = input()
            if fight != "3" or "run" not in fight.lower() or attempt != 0:
                print("She turns into a dragon and eats you")
                print("You died")
                dead = True
                kill_if_dead(dead)
            else:
                print("You run back to the other room")
                attempt = attempt + 1
                choice_2 = "left"
        else:
            print("You are kidding me, right? You want that?")
            print("The story teller killed you!!!")
            dead = True
            kill_if_dead(dead)


#########################################################################################################
# Willy and Justin
# Refactored by Team 19:                 #TODO Team 19 names here
# Google doc link:                       #TODO Team 19 Google doc link here
def team_19_adv():
    pass
    # TODO Add your code here


def main():
    """
    The main function, where the program starts.
    :return: None
    """

    username = start_story()
    paths = [sample_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(username)


main()