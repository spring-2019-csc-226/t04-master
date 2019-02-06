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
# Refactored by Team 7: Minh, Lisandro, Megan                #TODO Team 7 names here
# Google doc link: https://docs.google.com/document/d/1v0xL0OgO6_Z8l74_Gmb7Gg-4M28DCPIOM4q7xRe5ApY/edit?usp=sharing                    #TODO Team 7 Google doc link here

def team_7_adv():
    global dead
    print("You're walking through a jungle, looking for treasure when suddenly, something hard hits your head"
          + "and you fall to the ground.\n")
    sleep(delay * 5)
    print("When you wake up, you hear dark chanting coming from within the depths of the jungle.")
    sleep(delay * 2)
    print(" OO AHH AHH AHH, OO AHH AHH AHH")
    sleep(delay * 2)
    print("Looking around, you see a tribe of indians surrounding you and a giant fire in the middle of the circle. "
          + "The leader walks up to you and asks what your purpose is")

    answer = input("What do you tell him? {Truth/Lie} ")
    if answer == "Truth":
        # Bad choice
        print("'I was sent to look for treasure.'")
        sleep(delay * 2)
        print("The tribe of indians get angry and decide they must get rid of you!")
        print("They pick you up and start heading toward the fire...\n")
        dead = True

    else:
        # We lie!
        print("' I am lost. I am just trying to find my way out of the jungle.'")
        print("The leader looks at you and tells you he will leave you overnight and decide what to do with you" +
              " when tomorrow comes.")
        sleep(delay * 5)

    if dead:
        print("Oh!! What a horrible way to die. Better luck next time!")
        quit()

    print("Little does the leader know...")
    print("You have had a knife in your pocket the whole time")
    print("While the indians are done with you for the night, you cut yourself free, but hold the ropes" +
          " so you do not look suspicious.\n")
    sleep(delay * 3)

    print("You are thinking of ways to escape. You come up with three options: ")
    print("You can wait until the leader gets close and attack him and fight your way to freedom.")
    print("You can wait until everyone is asleep and then quietly make your escape.")
    print(
        "You can tell the leader that you want to be a part"
        " of the tribe and try to figure out your escape from there.\n")
    sleep(delay)

    option = input("Which option do you choose? [Attack/Wait/Join] ")
    sleep(delay)

    if option == "Attack":
        # Bad choice
        print("You wait until the tribe leader walks in front of you and then...")
        sleep(delay)
        print("You take your knife and stab him, killing him")
        print("You try to run, but the rest of the tribe gets to you first and kill you for killing their leader.\n")
        dead = True

    elif option == "Wait":
        # good choice
        print("So you sit there...waiting until everyone goes to sleep.")
        print("Once you see the last person has finally fallen asleep, you decide to make your move.")
        print("You quietly slip out of the ropes and creep away from the tribe")
        sleep(delay * 3)
        print(
            "You have been walking through the jungle for hours "
            "when suddenly you run into someone...another adventurer!")
        sleep(delay)

    else:
        # Neural choice
        print("You call the leader of the tribe over to you.")
        print("'I do not have anywhere to go. I was wondering if I could possibly join your tribe")
        print("The leader says a decision will be made later that night during the Ceremony...\n")
        # later that night
        print("The Ceremony has begun and the whole tribe is doing their chant...\n")
        sleep(delay * 3)
        print("OO AHH AHH AHH, OO AHH AHH AHH")
        sleep(delay)
        print("The leader yells 'SILENCE!!!!' " + username + "'wants to join our tribe.'")
        print("'I have decided that we shall give " + username + " a chance'")
        print("'We shall teach " + username + " our ways'\n")
        sleep(delay * 5)
        print("You are set free, but now you have to be a part of the tribe")

    if dead:
        print("Oh!! What a horrible way to die. Better luck next time! ")
        quit()

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