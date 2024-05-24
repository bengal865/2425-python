# Programmer: Bruce Provencher
# Date: 09 NOV 2016
# Project: Functions Test

import sys, time

def show_intro():
    print("Welcome to my Game Summary Generator!")
    time.sleep(2)
    print("This script will display info about characters in your game or player stats.")
    time.sleep(2)
    print("When prompted, please choose a menu option.")
    time.sleep(2)

def show_menu():

    print("""
    1. Display info about game character.
    2. Display player game stats.
    3. Quit

    """)

    char1 = ["Cicero", "lethal jester", "Falkreath Sanctuary"]
    char2 = ["Falion", "conjuration trainer", "Morthal"]
    char3 = ["Muiri", "alchemist apprentice", "Markarth"]

    stats1 = [750, 500, 300]
    stats2 = [1000, 700, 850]
    option = int(input("Please select a menu option: (1, 2 or 3):\n"))


    if option > 0 and option < 3:
        if option == 1:
            character_data = int(input("Choose a game character (1, 2 or 3 only):\n"))
            if character_data == 1:
                print ("Character's name: " + char1[0])
                print ("Character's profession: " + char1[1])
                print ("Character's location: " + char1[2])
            elif character_data == 2:
                print ("Character's name: " + char2[0])
                print ("Character's profession: " + char2[1])
                print ("Character's location: " + char2[2])
            elif character_data == 3:
                print ("Character's name: " + char3[0])
                print ("Character's profession: " + char3[1])
                print ("Character's location: " + char3[2])
            else:
                print("Invalid selection! Please try again!")
        elif option == 2:
            stats_choice = int(input("Display game stats for Player 1 or Player 2? (1 or 2):\n"))
            if stats_choice == 1:
                list_sum = sum(stats1)
                list_length = len(stats1)
                avg_score = list_sum / list_length
                max_score = max(stats1)
                low_score = min(stats1)
                print("\n\nAll scores for Player #1:" + str(stats1))
                print("Average score for Player #1: " + str(avg_score))
                print("High score for Player #1: " + str(max_score))
                print("Low score for Player #1: " + str(low_score))

            elif stats_choice == 2:

                list_sum = sum(stats2)
                list_length = len(stats2)
                avg_score = list_sum / list_length
                max_score = max(stats2)
                low_score = min(stats2)
                print("\n\nAll scores for Player #2:" + str(stats2))
                print("Average score for Player #2: " + str(avg_score))
                print("High score for Player #2: " + str(max_score))
                print("Low score for Player #2: " + str(low_score))

        elif option == 3:
            sys.exit()

        else:
            print("Try again! Your menu options are 1, 2 or 3 only!")
            show_menu()
        show_menu()

play_status = "yes"

while play_status == "yes" or play_again == "y":
    show_intro()

    show_menu()

    quit_now = input("Are you sure you want to quit? (y/n):\n")
    quit_now = quit_now.lower()

    if quit_now == "y" or quit_now == "yes":
        print("Thanks for playing today!")
        sys.exit()




