# Your Hallway
import os


def run():
    import main
    options = {"look around": 1, "look": 1, "check": 1, "leave": 2, "shop": 2}
    global_options = {"pick nose": "don't pick your nose"}

    # print(main.testvar)
    # main.testvar = 5
    print("You enter the hallway...What do you do?")
    option = input()

    for key in options:
        if option in options:
            option = options[option]
            break
        else:
            option = 4

    while option != 0:
        if option == 1:
            print("This is the hallway you see pictures")
        elif option == 2:
            print("You leave the hallway and continue on your way to the local shop.")
            return 3
        elif option == 4:
            print("You can't do that!!")

        print("What do you do?")
        option = input()

        for key in options:
            if option in options:
                option = options[option]
                break
            else:
                option = 4

