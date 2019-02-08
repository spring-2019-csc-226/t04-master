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
# Refactored by Team 17: Tristan Weir, Azariah Mawoko, Wilkensley Thervil.
# Google doc link: https://docs.google.com/document/d/14k7q9gxd21NPqNXWMXrJZ1hzWOlmyoELNKOJb_n85V8/edit?usp=sharing
def team_17_adv():
    global username
    global dead
    # Start of our code.
    # gets input from the user, 1 2 or 3 for simplicity. Could do rock, sword, or cave.
    print("You appear in a cave. It is dark, and smells weird. You look around...")
    sleep(2)
    print(
        "You hear a growling sound coming from deeper in the cave. \nYou see a sword, a mysterious glowing green rock.")
    print()
    # we can either use a loop to handle 'incorrect' choices, or an else to catch anything we didn't think of.

    # get input from user, present options, and store that as a string

    opt1 = input("""What would you like to do?\n 
    1. Pick up sword to fight off the growling monster.\n
    2. Investigate the mysterious rock.\n
    3. Venture deeper into the cave to try to reason with the monster.\n 
    Press 1, 2, or 3 depending on your choice, or type a command.""")

    # type cast the user's input as a string, and make all characters in that string lowercase.
    choice = str(opt1).lower()

    # neutral choice

    # the user can either enter 1, sword, or fight to get this option.
    if '1' in choice or "sword" in choice or "fight" in choice:
        print("""You pick up the sword, attempt to fight the monster, \n
        You manage to kill the monster, but you are badly wounded in the process. You are able to continue on.""")
        sleep(delay)
        print("""You see a growing red flask on the ground.\n
              Do you want to drink the strange liquid you found in a cave? Yes or No?""")
        opt2 = str(input("What do you want to do?")).lower()

        # special case, check if the user is named 'emily', or 'azis' and if so, do a special thing.
        if 'emily' in username.lower() or 'azis' in username.lower():
            print("A wizard changed your name. You are hereafter known only as The Old Man.")
            username = "The Old Man"
        # if user wants to drink the potion, or the liquid
        elif 'drink' in opt2 or 'potion' in opt2 or 'liquid' in opt2 or 'yes' in opt2:
            sleep(delay)
            print("seriously?")
            print("...")
            sleep(delay * 2)
            print("""You weirdo. \n 
            You literally found that on the floor of a cave...
            \n You drink the liquid, and it kills you.""")
            # they died, change the variable to reflect that.
            dead = True
        elif 'nothing' in opt2 or 'no' in opt2:
            sleep(delay * 3)
            print("Good choice. \nOnly a weirdo would drink liquid they found on the floor of a cave, right?")
            sleep(delay * 2)
            print("RIGHT...?")
            sleep(delay * 2)

            # catch any other input here. Kill them off
        else:
            sleep(delay * 2)
            print("You roll off a ledge of a hidden cliff, and die.")
            dead = True
    # positive choice
    elif '2' in choice or "rock" in choice or "touch" in choice:
        print("""You touch the magic rock, and you are teleported to a mysterious room.""")
        sleep(delay * 2)
        print("It is the living room of a fancy mansion.")
        mansiontest = False
        mansionring = False
        mansioncheck3 = False
        while not mansiontest:
            print("There are 3 doors, 2 windows, and a Piano as well as some other furniture of little importance.")
            mansionchoice = input("What would you like to do?\n [Door 1/2/3] [Window 1/2] [Piano]")
            if 'piano' in mansionchoice.lower() and 'play' in mansionchoice.lower():
                print("You play a tune that you didn't know you could play.\n Congrats " + username + "!!!")
                sleep(delay)
            elif 'piano' in mansionchoice.lower():
                print("It is a very nice Piano!")
                print("You should try playing it!")
                sleep(delay)
            elif 'door' in mansionchoice.lower() and '1' in mansionchoice.lower():
                print("You opened door 1!!!")
                sleep(delay * 2)
                print("You find the owner of this mansion...")
                print("He is not happy...")
                sleep(delay)
                print("He stabs you with his knife.")
                print("You bleed out.")
                dead = True
                mansiontest = True
                sleep(delay)
            elif 'door' in mansionchoice.lower() and '2' in mansionchoice.lower():
                print("You opened door 2!!!")
                sleep(delay * 2)
                print("It is another room.")
                print("You walk in.")
                sleep(delay)
                print("And everything goes white.")
                mansiontest = True
                sleep(delay)
            elif 'door' in mansionchoice.lower() and '3' in mansionchoice.lower():
                print("You opened door 3!!!")
                sleep(delay * 2)
                print("Behind this door there is another door.")
                print("You open that door.")
                sleep(delay)
                if mansionring:
                    print("You see another room.")
                    if mansioncheck3:
                        print("Wait. Was this here before?!")
                        sleep(delay)
                    print("This room is like nothing you have seen before.")
                    sleep(delay)
                    print("You decide to go through.")
                    sleep(delay)
                    mansiontest = True
                else:
                    print("There is an additional door behind that door.")
                    print("You decide to stop and close all doors you just opened.")
                    mansioncheck3 = True
                    sleep(delay)
            elif 'window' in mansionchoice.lower() and '1' in mansionchoice.lower():
                print("You look through window 1!!!")
                sleep(delay * 2)
                print("It is dark outside...")
                print("Too dark to see anything...")
                sleep(delay)
                print("The darkness stares back at you...")
                sleep(delay)
                print("You witness unspeakable horrors...")
                sleep(delay)
                print("And you slip...")
                sleep(delay)
                print("Into Madness...")
                mansiontest = True
                dead = True
            elif 'window' in mansionchoice.lower() and '2' in mansionchoice.lower():
                print("You look through window 2!!!")
                sleep(delay * 2)
                print("It is very dark outside.")
                print("You can't see anything.")
                sleep(delay)
                print("You have a feeling that there is something in the furniture.")
                print("It is just a feeling, though.")
                sleep(delay)
            elif 'furniture' in mansionchoice.lower():
                print("You check through the furniture")
                sleep(delay * 2)
                print("You find ring.")
                print("It fits you perfectly!")
                sleep(delay)
                print("You decide to take it with you.")
                print("It may prove useful later.")
                sleep(delay)
                mansionring = True
            else:
                print("You did nothing!")
                print("Please try again.")
                sleep(delay)
    else:
        print("""Confused, you venture deeper into the cave, and try to talk to the monster.""")
        sleep(delay)
        print("""Thinking the monster wanted a hug, you go in to embrace it, and it eats you.""")
        dead = True

    # at the end, check if user is dead or not.
    if dead:
        sleep(delay)
        print("Sorry " + username + ".\n You have died. \n Better luck next time!")
        # we don't need to add an else statement before the lines after this,
        # as the "quit()" function will end the program.
        quit()


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