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
# Refactored by Team 16:                 #Justin and Heremes
# Google doc link: https://docs.google.com/document/d/1Roq1OdFZ9eDMyAFj184HY3wK8MZniQx_X01FXFm_FrE/edit?usp=sharing
def team_16_adv():
    global dead
    print("You enter into the abandoned cabin, trying to find a place to rest for the night.")
    sleep(delay)
    print("You go to the table to start unpacking, first your backpack, and then your water.")
    sleep(delay)
    print("After a few minutes of trying to get your stuff set up and a fire going for the night, you begin to "
          "hear heavy footsteps outside")
    sleep(delay*2)
    print("Quick! Where to hide at?")

    choice = input("Under the Table, Closet, Don't move, Play dead, ")
    if choice == "Table" or choice == "table":
        print("You get under the Table, trying to make no noise.")
        sleep(delay)
        print("In through the Cabin door comes a bear! It stops, and begins sniffing the room")
        sleep(delay)
        print("It walks over to the table, stopping in front of it and growling. Uh oh, you think it's found you.")
    elif choice == "Closet" or choice == "closet":
        print("You scramble to the closet, shutting it, keeping it just open enough to peek outside.")
        sleep(delay)
        print("In through the Cabin door comes a bear! It stops, and begins sniffing the room")
        sleep(delay)
        print("It lumbers over to the closet, clawing at the door and roaring. Uh oh, you think it's found you.")
    elif choice == "Stand still" or choice == "stand still" or choice == "Stand Still":
        print("You hold your ground, staring at the door anxious.")
        sleep(delay)
        print("In through the Cabin door comes a bear! It stops, and stares directly at you, roaring.")
    elif choice == "Play dead" or choice == "play dead" or choice == "Play Dead":
        print("You drop to the floor, trying to be as still as you can be.")
        sleep(delay)
        print("In through the Cabin door comes a bear! It stops, and begins sniffing the room")
        sleep(delay)
        print('''The bear walks over to you. You can only assume it noticed your breathing,
            it's roared and scared you to your feet.''')
    sleep(delay*2)
    print("The bear seems to charging up a swing at you! ")
    choice = input("Will you: Dodge, Attack, or Block? ")
    if choice == "Dodge" or choice == "dodge":
        print("The bear lunges at you, and you side step the attack.")
    elif choice == "Block" or choice == "block":
        print("The bear lunges at you, you hold up your shield and the bears claw's deflect off of it")
    elif choice == "Attack" or choice == "attack":
        print("You swing your sword at the bear and catch it in the arm!")
        sleep(delay)
        print("You feel pretty good about yourself until the bear cracks your skull with it's claw")
        dead = True
    if dead:
        sleep(delay)
        print("Your story ends there, Bear food.")
        quit()
    else:
        sleep(delay)
        print("The bear's claws whizzes by your head in a second swing. The bear falls and you stick your sword"
              " through it's skull, Good job! You finally now have a moment to relax and eat.")

    # Secondary Assignment

    if not dead:
        sleep(delay)
        print("Now it's time to divide your Rations for the day")
        sleep(delay)
        choice = int(input("You have 8 Rations remaining, how many are you going to cook? "))
        if choice >= 1 <= 2:
            print("Not a whole lot, but enough to keep you going for the day, you assume. You'll have to wait and see")
        elif choice >= 3 <= 5:
            print("You're cooking a fair bit of your Rations. Let's hope you find more, or have enough for the week.")
        elif choice >= 6 <= 8:
            print("At least you'll eat well tonight, you better hope it was worth it.")
        elif choice >= 9:
            print("Ambitious huh? You don't have that many Rations. You cook as many as you can.")
        elif choice <= 0:
            print("None huh? Guess you're trying to keep some, smart.")
        else:
            print("You're so unsure of how many to cook, you don't cook any, you'll just go hungry tonight.")


#########################################################################################################
# Ben and Luis
# Refactored by Team 17:                 #TODO Team 17 names here
# Google doc link:                       #TODO Team 17 Google doc link here
def team_17_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Minh and Taran
# Refactored by Team 18:                 #TODO Team 18 names here
# Google doc link:                       #TODO Team 18 Google doc link here
def team_18_adv():
    pass
    # TODO Add your code here


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