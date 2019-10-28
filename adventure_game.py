import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def random_choice():
    return random.randint(0, 9)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause("Sorry, I don't understand. Make your "
                        "choice between {} or {}.".format(option1, option2))
    return response


def play_again():
    response = valid_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n", "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, let's start again!")
        choose_path()
    else:
        print_pause("Please say yes or no")


def game_over():
    print_pause("GAME OVER\n")
    play_again()


def intro():
    print_pause("You promised to visit your Aunt Diana.")
    print_pause("She lives in a secluded place, in the country side.")
    print_pause("You're on your way by car.")
    print_pause("Suddenly, your car breaks down halfway!")
    print_pause("You'll have to go on foot.")
    print_pause("There are two roads in front of you.")
    print_pause("The two take to your Aunt's house, "
                "but they have a different route.")
    print_pause("You don't remeber which one is the best or the safest.")
    print_pause("But you must choose one and it's getting dark...")
    print_pause("You don't want to be outside at nightime in these areas...")
    print_pause("You have heard disturbing rumors in your "
                "childhood about witches, ghosts and "
                "monsters living in these woods.")
    print_pause("So you decide to choose one road and go "
                "walking as fast as possible to your Aunt Diana's house.")


def choose_path():
    print_pause("As said before, there are two paths, "
                "which path do you choose?")
    road = valid_input("Please enter right or left:\n", "right", "left")
    if road == "right":
        right_path()
    elif road == "left":
        left_path()


def right_path():
    print_pause("Okay! The right one, of course.")
    print_pause("You go fast and cautious by this way, "
                "but after 20 minutes walking you see a snake on the road,")
    print_pause("the road is narrow, so you need to pass "
                "close to the snake and maybe the snake will bite you.")
    print_pause("Could be a poisonous snake, but you don't know that.")
    print_pause("Do you want to try to pass anyway "
                "or do you want go back to the car?")
    action = valid_input("Please enter pass or go back:\n", "pass", "go back")
    if action == "pass":
        if random_choice() in [0, 1, 2]:
            print_pause("the snake bites you! Oh, my god!")
            print_pause("It was a poisonous snake. You are "
                        "going to be dead in just a few minutes.")
            game_over()
        else:
            print_pause("The snake bites you! Oh, my god!")
            print_pause("But it wasn't a poisonous snake, after all.")
            print_pause("Even with a little pain you decided "
                        "to continue anyway.")
            witches()
    elif action == "go back":
        print_pause("Okay, you decided to go back to your car, "
                    "but the sun went down and now it's nightime.")
        print_pause("After some walking back to your car, do "
                    "you see what do you think "
                    "that is a ghost coming from far.")
        print_pause("You can run or you can stay and waiting "
                    "and try to talk with him. What do you want to do?")
        action_2 = valid_input("Please enter run or wait:\n", "run", "wait")
        if action_2 == "run":
            print_pause("You run for your life, praying.")
            print_pause("...")
            print_pause("And you escape. The ghost couldn't "
                        "catch you and disappear.")
            print_pause("So you continue your path to your Aunt's House.")
            print_pause("You notice that the snake is not on "
                        "the middle of the path anymore, that is a good sign.")
            print_pause("You guess.")
            witches()
        elif action_2 == "wait":
            if random_choice() in [0, 3, 5]:
                print_pause("The ghost was sad and angry...")
                print_pause("but after talking with you, the ghost "
                            "says that he feels so much better, "
                            "say thanks for you hearing him and leave.")
                witches()
            else:
                print_pause("That ghost was really angry.\n")
                print_pause("You are doomed.\n")
                game_over()


def left_path():
    print_pause("You took the left path.")
    print_pause("After half hour walking you think "
                "that you took the bigger path,")
    print_pause("that sucks, but at this point do you think "
                "is better to continue than go back.")
    print_pause("Soon the nightime comes and it's a fullmoon night.")
    print_pause("Do you hear a howl coming from the woods around the road.")
    print_pause("Right after that a werewolf appears "
                "out of nowhere and jumps just in front of you!")
    print_pause("You can run or you could stay "
                "and try to know more about this mythical criature.")
    action_3 = valid_input("Please enter run or stay:\n", "run", "stay")
    if action_3 == "run":
        print_pause("You run for your life, praying!")
        print_pause("And you escape from the criature!")
        print_pause("What a relief you feel when you notice that now,")
        print_pause("after all this running from the monster,")
        print_pause("you are close to your Aunt's house.")
        witches()
    elif action_3 == "stay":
        print_pause("You stay at the same place and don't mind to run.")
        print_pause("Do you want to understand more "
                    "about this amazing and rare criature.")
        print_pause("Unfortunately, the werewolf don't "
                    "want to colaborate and talk with you.")
        print_pause("You are doomed.\n")
        game_over()


def witches():
    print_pause("After some more time walking, "
                "do you feel now that landscape is familiar...")
    print_pause("Do you remember this part of the way!")
    print_pause("And now you are sure that you "
                "are close to your Aunt's house.")
    print_pause("You're keep walking and calculate that "
                "you are just a few minutes by walking from her house.")
    print_pause("Suddenly, you see from distance a witch!")
    print_pause("She seems mad, she seems disturbed, "
                "but she is far, who knows for sure?")
    print_pause("You can run (again) or you "
                "can stay and try to talk with her.")
    action_4 = valid_input("Please enter run or talk:\n", "run", "talk")
    if action_4 == "talk":
        if random_choice() in [2, 6]:
            print_pause("You speak with her, she feels better, "
                        "she says goodbye and let you pass.")
            print_pause("Do you finally get to your Aunt Diana house!")
            print_pause("Do you encounter you Aunt Diana, "
                        "inside of her house.")
            print_pause("You two have a great dinner, good "
                        "talk and a lot of laughs.")
            print_pause("You sleep in her house and at morning "
                        "you will go back to your car and life.")
            print_pause("(Next day, at morning)")
            print_pause("Now it is daytime and in the daytime "
                        "the roads are very safe in this region.")
            print_pause("You are happy to have had seen "
                        "your dear Aunt Diana and the "
                        "best of all: you are still alive.")
            print_pause("Victory!")
            play_again()
        else:
            print_pause("She is very angry, indeed.")
            print_pause("You try to talk with her.")
            print_pause("She doesn't listen you, she just screams.")
            print_pause("You are doomed.\n")
            game_over()
    if action_4 == "run":
        print_pause("You run! Praying! Asking to all the gods for protection!")
        print_pause("It doesn't seem enough to avoid "
                    "the witch to come after you.")
        print_pause("Right when the witch is going to catch you, ")
        print_pause("your Aunt Diana suddenly appears!")
        print_pause("She is a witch too, but she is a "
                    "good one. She saves you from the other witch.")
        print_pause("Aunt Diana brings you to her home "
                    "and you two have a great dinner, "
                    "good talk and a lot of laughs.")
        print_pause("You sleep at her house and at "
                    "morning you will go back to your car and life.")
        print_pause("(Next day, at morning)")
        print_pause("Now it is daytime and in the daytime "
                    "the roads are very safe in this region.")
        print_pause("You are happy to have had seen your "
                    "dear Aunt Diana and the best "
                    "of all: you are still alive.\n")
        print_pause("VICTORY!\n")
        play_again()


def play_game():
    intro()
    choose_path()


play_game()
