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
# Refactored by Team 6:                 #TODO Team 6 David Reynoso and Evan Horsley
# Google doc link:                      #TODO Team 6 https://docs.google.com/document/d/1lVaSKzBsf-wlLdDJVvwkwkA6EALrBiCw4vmcJzR7BYQ/edit?usp=sharing
def team_6_adv():
    global dead
    direction = input("Which direction would you like to go? {South, West }")

    if direction == "South":
        # right choice.
        print("You locate a stream of water on the floor. Following it could lead you to the exit.")
        sleep(delay)
        print("you set up camp next to the stream and go to sleep")
        sleep(delay)
        print("...")
        sleep(delay)
        print("...")
        sleep(delay)
    elif direction == "East":
        # Wrong choice
        print("In the darkness, you fail to see a sinkhole that you fall into, never to escape.")
        print('')
        num = int(
            input("Before falling to your doom, you reach out into the darkness and attempt to grab onto the edge."
                  " How far do you extend your arm? (1-90)"))
        if num < 45:
            print('You did not reach out far enough, therefore you fell to your death.')
            dead = True
        elif num > 90:
            print('your arm gets ripped out of its socket and you fall to your death')
            dead = True
        elif num > 45:
            print('you grabbed onto a ledge and pulled yourself up')
    else:
        # neutral choice
        print("You continue your travel but you're as equally confused as you were moments ago.")
        sleep(delay)
    if dead:
        print("You are banished to the sinkhole for the rest of your days. Better luck next time!")
        quit()


#########################################################################################################
# Kenzie and Caleb
# Refactored by Team 7:                 #TODO Team 7 names here
# Google doc link:                      #TODO Team 7 Google doc link here
def team_7_adv():
    pass
    # TODO Add your code here


#########################################################################################################
# Liberty and Joseph
# Refactored by Team 8:                 #Johnathan West and Caleb Schaller
# Google doc link:                      #https://docs.google.com/document/d/1Cp1PgZYSR_yV38XJeLj0LyTgzhJ0FLIfJxyJXtiUGh4/edit?usp=sharing
def team_8_adv():
    global dead
    # A Haunted house with four doors and each doors leads to different destination
    print()
    print("You are trapped in a haunted house with four doors")
    print("Some doors will lead you out to go home and others let you to the voracious\n and unmerciful Creatures")
    print("Each door leads to a different destination, and you have to avoid the evil door in order to stay alive")
    print()

    direction = input("which door would you like to pass through? [door1/door2/door3/door4]")

    if direction == "door1":
        # Door1 Oh Nooo.. you just made a bad choice!
        print("You just opened the evil door .")
        sleep(delay)
        print("This door leads to a room filled up with thousands of zombies.")
        print("It is difficult to survive among these zombies")
        print("You have no choice than to be eaten up by the zombies")
        print("Your blood taste like an orange juice, and your flesh taste like a barbecue chicken to the zombies")
        dead = True
        # Door2 Comprises of good and bad choices
    elif direction == "door2":
        print("Wow!!! You have  made a wonderful choice but you have to enter a code  \n on the door")
        print("There are two codes in front of the door, one among the two codes exits you from the haunted house")
        print("The other code opens the door for hungry Snakes into the room")
        choice = input(' Enter code 1 or 2 on the door locker')
        x = int(choice)
        if x == 1:
            print("You are Lucky!!! Go out and never come back to this area again")
            print("Congratulations, you survived the haunted house alive")
        elif x == 2:
            print("ALERT!! WRONG DOOR!!")
            print("You just opened the door for two massive python snakes")
            sleep(delay)
            print("Say your last words before you find yourselves in our stomachs")
            print("You are now Dead")
            dead = True
    # Even or odd number decision keep you alive or dead
    elif direction == "door4":
        print("This is the worst door. but there are still options to make towards your survival")
        print("However in this section you will need to pick a number, "
              "the right number will extend your chance of living")
        option = input("enter any number you like")
        x = int(option) % 2
        if x == 0:
            print("You entered an even number which closes the gate, and prevent the deadly animals from entering.")
            print("However you are still in the room but safer than if you had proceeded with that way.")
        elif x == 1:
            print("You entered an odd number")
            print("The dragon will now feed on you")
            print(" You are Dead without any further travel!!! ")
            dead = True
    # The best option to make
    elif direction == "door3":
        print(" You are now safe")
        print("this door automatically get you out of the haunted house")
        print("Look at that! You made it safe without being killed! ")
        print("Congratulations... now go play again and explore every other door in the haunted house.")
    kill_if_dead(dead)

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
# Refactored by Team 11:    #Nmasichi Chukwuemeka, Trent Powell, Alex Craig
# Google doc link:          #https://docs.google.com/document/d/1k3iU9IosNd8sYJ2kfGhNvTCngZ5HTC0qKnabXkCH3Vo/edit?usp=sharing
def team_11_adv():

    global dead             # You'll need this to be able to modify the dead variable
    if dead is False:
        print("After hours of wandering in the cave you met Indiana Jones")
        sleep(delay)
        print("He wants to help to search for a treasure")
        decision = input("Do you want to join him? {Join, Stay, Leave} ")

        if decision is "Join":
            print("Great, you found a treasure with Indiana Jones.")
            sleep(delay * 3)
            print()
            print("However, he really does not like to share.")
            sleep(delay * 3)
            print()
            print("When you turned around, he pulled out a gun and shoot you to your head.")
            dead = True
            # bad option
        elif decision == "Stay":
            print("Indiana Jones went the wrong direction and fell for a trap")
            sleep(delay * 3)
            print()
            print("You can hear boulder movements followed by bone cracking and human scream")
            sleep(delay * 3)
            print()
            print("Indian Jones died as a hero")
            # good option
        else:
            # neutral choice
            print("You left the place and you keep going deeper into the cave.")
            sleep(delay * 3)
            print("You do not know what happened with Indiana Jones")
            sleep(delay * 3)
            print("The story continues")

        kill_if_dead(dead)
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
# Refactored by Team 13: Mahmoud Amer & Kabelo Makotoko
# Google doc link: https://docs.google.com/document/d/1qI99v-PuIQuvPOnEpo0BYnBpGkNwSCrQeMppp-L2yRE/edit?usp=sharing
def team_13_adv():

    global dead
    print("You choose to leave the cave.\n")
    sleep(delay)
    print("The first thing that you see when exiting the cave is a demonic tornado from hell!")
    print("As the tornado rages on you notice a tank not too far away.\n")
    choice = input("Your options are either to FIGHT, RUNAWAY, or to TANK.\n").lower()
    if choice == "fight":
        print("As you approach the tornado, hands up screaming your battle cry, you are sucked up into it.")
        print("You burn alive as your limbs are ripped from your body.\n")
        dead = True
    elif choice == "tank":
        print("You open up the tank hatch to find a little German man speaking Japanese")
        sleep(delay * 2)
        choice = input("You can either PUNCH him and take the tank or try to SPEAK Japanese back.\n")
        if choice == "punch":
            sleep(delay * 3)
            print("The man doesn't even flinch as your fist connects.")
            print("He draws his Luger and put 7 shots into your chest")
            dead = True
        elif choice == "speak":
            print("You mutter something that you think sounds like Japanese to the man.\n")
            sleep(delay * 2)
            print("He looks at you like you're an idiot and presses a button on the wall.\n")
            sleep(delay)
            print("The tank surprisingly fires a large burst of water from its cannon towards the tornado.\n")
            sleep(delay * 2)
            print("Congratulations, you survived the horrible fire tornado.")
            print("The German gives you a shiny pendant! You now continue on your journey into the unknown\n")
    elif choice == "runaway":
        print(" You chose to run back into the cave.")
        sleep(delay * 2)
        print("As you blindly sprint into the pitch black cave you slam into a cave wall.\n")
        sleep(delay)
        print("You fall to the ground and hit your head on a rock.")
        sleep(delay * 5)
        print("You wake up several hours later and don't remember anything")
    kill_if_dead(dead)



#########################################################################################################
# Nmasichi, Kabelo, and Christian
# Refactored by Team 14: Ben Turner, Jalen Prater
# Google doc link: https://docs.google.com/document/d/18nClywLE7ov2pp9qqSyUscz23Cxp4JegWD2ixIi0Yd4/edit?usp=sharing
def team_14_adv():
    global dead

    print(
        "Hello " + username + """ You are in heaven. 
        You noticed you have wings on your back and you have white clothes on.... 
        \n Kudos!!! You are an angel  """)
    direction = input(
        """where would you like to take your adventure to? You unworthy angel
         \n [East : You hear nothing]
         \n [West: You see a delicious looking apple]
          \n [South: You hear the cry of a child]
         \n [North: a woman screaming in agony]""")

    if direction == "west ":
        print(
            """You are tempted to eat the Golden apple because you have heard stories of the powers you can receive from it. 
            \n The moment you bite into the apple, you feel like you are on fire. 
            \n You look down at yourself and you see flesh lying around your feet covered in blood. 
            \n You feel like you are getting weak, like you may be on the verge of death. 
            \n God has no pity. He sends you to the gate separating hell from everything, which is guarded by a big three headed dog, Cerberus. \n Once Cerberus takes note of your scent, he quickly pounces on you. The middle head bit your arm clean off, and you scream in agony.\n Cerebrus takes its left paw with its sharp claws and stabs a hole in your stomach. \n You are unable to move and begin coughing out blood. \n Cerebrus then takes 2 claws and puts them in the hole he created and rips you straight in half spewing your blood everywhere. 
            \n You are dead   """)

            dead = True
    elif direction == "east":
        print(
            """You were not tempted by the other paths and so you are given the ability to see the near future. 
            \n God says that there is a catch so you can't consistently use it for greed .
            \n You may only be able to use this ability when you are nearest to death as it will allow 
            you the chance to preserve your life should you choose to do so. 
            \n God painlessly rids you of your wings. God decides to send you to earth to carry out a normal-ish human life. """)

        sleep(delay)
    else:
        print(
            """You search for what you heard and you realize there is no one. 
            You come to face Lucifer but you return to God. 
            \n God smites you because you were tempted by the worst of God's creations.
             God grabs both bases of your wings and without any mercy he rips them from your body.
              \n He then banishes your pathetic being to the likes of earth. """)
        sleep(delay)


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