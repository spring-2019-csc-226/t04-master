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
# Refactored by Team 3:  Thomas Brown, Eleni Lazaridou
# Google doc link:  https://docs.google.com/document/d/1Ht1q5ChzK7puaiLILkQ650FyQ9SSIXQ814VHqDUT_Yw/edit#

def team_3_adv():
    global dead
    print("You hear a large explosion from behind and your head hits the ground WHACK")

    for i in range(3):
        sleep(delay)
        print("...")
    print("Your eyes blur and you wake up in a cold, dark cellar. You see a collection of metal bars in front of you.")
    print("You realize you are in a jail cell.")

    if not dead:
        choice1 = input("What would you like to do? [look/escape]")
        if choice1.find("look") is not -1 and not 'dead':
            print("You see your bed, a small nightstand with a rubber duck sitting on top, and a small hole in the corner.")
        elif choice1.find("escape") is not -1 and not 'dead':
            print("You flail your arms through the prison cell bars screaming for attention.")
            sleep(delay)
            print("A guard dressed in full chain mail blazoned by the kings crest approaches you.")
            print("What is all this raquet for?! Silence!")
            print("He hits you over the head with his mace killing you instantly.")
            dead = True

    else:
        print("you waste away in prison and die of boredom")
        dead = True

    if not dead:
        choice2 = input("What will you do now? [squeak rubber ducky/pick up bedsheets]")
        if choice2.find("squeak") is not -1 and not dead:
            print("The sharp squeak of the small toy duck rings through the empty hall.")
            sleep(delay)
            print("...")
            sleep(delay)
            print("A guard dressed in full chain mail blazoned by the kings crest approaches you.")
            choiced = input("What will you do? [bargain/attack]")
            if choiced.find("bargain") is not -1 and not dead:
                print("You give the guard your best sales pitch: 'Will you let me out for this rubber ducky?'")
                print("The guard looks at you confused but agrees. The doors open up and you are free from the prison.")

            elif choiced.find("attack") is not -1 and not dead:
                print("you throw the small yellow duck at the guard")
                sleep(delay)
                sleep(delay)
                print("The guard is furious with you and swings his mace and kills you.")
                dead = True

            else:
                print("you waste away in prison and die of boredom")
                dead = True

        elif choice2.find("bedsheets") is not -1 and not dead:
            print("You take the bedsheets.")
            sleep(delay)
            print("A guard dressed in full chain mail blazoned by the kings crest approaches you.")
            choiceb = input("'What are you doing with those bed sheets?' What will you do? [bargain/attack]")
            if choiceb.find("bargain") is not -1 and not dead:
                print("You give the guard your best sales pitch: 'Will you let me out for these bed sheets?'")
                sleep(delay)
                print("The guard looks at you confused, 'how dare you address sir reginold the third in this way!.")
                sleep(delay)
                print("The guard is furious with you and swings his mace and kills you.")
                dead = True

            elif choiceb.find("attack") is not -1 and not dead:
                print("you lasso the bedsheets around the guardsman's neck and strangle him to death")
                sleep(delay)
                print("The guard falls limp you take the cell key and you are free")

        else:
            print("you waste away in prison and die of boredom")
            dead = True

    else:
        if not dead:
            print("you waste away in prison and die of boredom")
            dead = True
            quit()

    if dead:
        print("you were unable to escape ye old prison rest in peace")
        quit()
    if not dead:
        print("congratulations you have escaped prison")
        quit()




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

    # make the variable dead the same as the one used by all
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

    if "west" in direction.lower():
        print(
            """You are tempted to eat the Golden apple because you have heard stories of the powers you can receive from it. 
            \n The moment you bite into the apple, you feel like you are on fire. 
            \n You look down at yourself and you see flesh lying around your feet covered in blood. 
            \n You feel like you are getting weak, like you may be on the verge of death. 
            \n God has no pity. He sends you to the gate separating hell from everything, which is guarded by a big three headed dog, Cerberus. \n Once Cerberus takes note of your scent, he quickly pounces on you. The middle head bit your arm clean off, and you scream in agony.\n Cerebrus takes its left paw with its sharp claws and stabs a hole in your stomach. \n You are unable to move and begin coughing out blood. \n Cerebrus then takes 2 claws and puts them in the hole he created and rips you straight in half spewing your blood everywhere. 
            \n You are dead   """)

        # dead
        dead = True

    elif "east" in direction.lower():
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
    # if the character is dead, kill them, because that makes sense/
    kill_if_dead(dead)

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
# Refactored by Team 19: Sandesh Lamichhane, Lesley Knox
# Google doc link: https://docs.google.com/document/d/1t2CauURVe-mGNAmSKxBVAQC90mN1WN6lSDrQYZzrEV4/edit?usp=sharing
def team_19_adv():

    global dead

    sleep(delay)
    print()
    print('You see 3 boxes in the path. You have an innate curiosity of what resides in those boxes.')
    boxes = input("What would you like to do? (Open Right, Open Middle, Open Left, Keep Walking.)")
    sleep(delay)
    if boxes == "Open Right":
        sleep(delay)
        print()
        print('A cat pops out and claws your eye out!')
        print("Talk about a bad day! You are now only capable of seeing half as well!")
        sleep(delay)
    elif boxes == "Open Middle":
        sleep(delay)
        print()
        print('A leprechaun pops out with a flamethrower. You have been burned by the Irishman!')
        dead = True
    elif boxes == "Open Left":
        print()
        sleep(delay)
        print("A happy leprechaun pops out, hands you a shiny golden piece, and leads you on his happy journey home!")
    else:
        sleep(delay)
        print("You continue walking in the darkness ahead, fearful of what resides in the boxes. You are still lost.")
    if dead is True:
        print()
        print('You have died! By a leprechaun! HAHAHAHAHAHAHAHAHAHAHA!!!!')
        quit()


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
