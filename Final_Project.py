# ######################################################################
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
import turtle
from time import sleep


class Labyrinth:
    def __init__(self, state, goodcall, statecounter, goodcounter, room):
        self.goodlist = ['Hoorah! ', 'Great Choice!', 'Bow Chick a Wow Wow!']
        self.goodcall = goodcall
        self.state = state
        self.goodcounter = int(goodcounter)
        self.statecounter = int(statecounter)
        self.room = room

    def change_call(self):
        if self.goodcounter % 5 == 0:
            self.goodcall = random.choice(self.goodlist)

    def report(self):
        if self.statecounter == 10:
            self.state = 'Too ill to carry on...'
        elif self.statecounter == 2:
            self.state = 'I am feeling dizzy. '
        else:
            self.state = 'This is exciting! '

    def random(self):
        good = "good"
        nuetral = "neutral"
        bad = "bad"
        roomlis = [good, bad, nuetral]
        newroom = random.choice(roomlis)
        self.room = newroom
        if newroom == "neutral":
            self.statecounter += 1


delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!


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


###################################################################################


def lab():
    l = Labyrinth('', '', 0, 0, '')         # Sets up class
    l.random()                              # Randomly selects what kind of room you wil go to.
    room = random.randint(0, 2)             # Chooses a random int to be used to get a random item from lists.
    goodlis = ["You find your way out of the cave into a paradise of sexy people. They see you as the god they were"
               " waiting to emerge from the darkness within. The people begin to shower you with praise and take you to"
               " the throne in which they prepared for you, their king. ",
               "Upon exiting the cave you fall a long ways. It felt like several minutes had gone by before you landed "
               "in this giant tub of water. After pulling yourself out of the tub you realize that you had just found "
               "yourself in the Bat Cave! ",
               "You exit the cave in time to find yourself in te middle of the a rock concert and you are on stage. "
               "You meet your favorite rock singer. All the excitement leads you to \njump out into the crowd to be "
               "crowd serfed for the duration of the concert."]
    badlis = ["You exit the cave and fall for what feels like an eternity . Then before you know it...splat!",
              "You exit the cave to find yourself being targeted as the prime figurehead for paparazzi. At first "
              "this is very flattering and even strike a pose and then realize you are only in your underwear. ",
              "You exit the cave in time to be shot in the side of the head by the assassin hunting you down."]
    neutrallis = ["You exit the cave to see an amazing sight... more cave!",
                  "As you run through the exit of the cave you don't notice there is a hill and you trip and disalign"
                  "your hips. ",
                  "You exit the cave just to be greeted with an apocalypse you now have to survive. Is Chloe "
                  "your baby sister still alive? "]
    l.report()

    if l.room == "good":
        l.goodcounter += 1
        l.change_call()
        print(goodlis[room] + l.goodcall)
        print(l.state)

    if l.room == "bad":
        l.statecounter = 10
        l.report()
        print(badlis[room])
        print(l.state)
        suicide()                   # Kills user
    if l.room == "neutral":
        l.statecounter = 2          # Sets the state counter to 2 in order to change the state of the character.
        l.report()                  # Changes the state based on counter.
        print(neutrallis[room])
        print(l.state)


def suicide():
    quit()


def keypress(wn):
    wn.onkey(suicide, "q")
    wn.onkeypress(lab)
    wn.listen()


def adventure(wn):
    """
    Original adventure text given as an example. Leave it alone as well.
    :return: None
    """
    wn = turtle.Screen()
    print("Which direction would you like to go? [North/South/East/West])")
    keypress(wn)


def main():
    wn = turtle.Screen()
    start_story()
    adventure(wn)
    wn.mainloop()


main()


