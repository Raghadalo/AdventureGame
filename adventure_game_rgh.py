import time
import random


def print_p(msg_print):
    print(msg_print)
    time.sleep(2)


def intro():
    print_p("How are you, welcome to the maze.")
    print_p("In front of you two doors to out of the maze.")
    print_p("But to cross the first door must you get the password.")
    print_p("To cross the second door, you need the card.")
    print_p("The password and card be chosen randomly.")
    print_p("Good luck.")


def choose(cross):
    chos = input("\nPlease enter '1' , '2':\n")
    if chos == '1':
        door_one(cross)
    elif chos == "2":
        door_two(cross)
    else:
        choose(cross)


def door_one(cross):
    print_p("\nDo you have the password?")
    print_p("let's see what you have,\n " + cross)
    if cross == 'password':
        print_p("You have the password, you can cross..")
    else:
        print_p("You don't have the password, sorry you can't cross")
    play_again()


def door_two(cross):
    print_p("\nDo you have the card?")
    print_p("let's see what you have,\n " + cross)
    if cross == 'card':
        print_p("Great you have the card, go ahead you can cross.")
    else:
        print_p("sorry, you can't cross because you don't have the card")
    play_again()


def play_again():
    again = input("Do you want to play again? 'yes' or 'no'!:\n ")
    if again == 'yes':
        print_p("You are active ..")
        play_game()
    elif again == 'no':
        exit(print_p("GOODBYE!"))
    else:
        print_p("Please enter 'yes' or 'no'")
        play_again()


def play_game():
    intro()
    cross = random.choice(["password", "card"])
    choose(cross)
    play_again()


play_game()
