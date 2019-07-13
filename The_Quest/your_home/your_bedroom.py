    # Your Bedroom
    # import variables
    # import import osmain
    # import os

#

def run():
    import main
    wake_up_options = {"look around": 1, "look": 1, "check": 1, "leave": 2, "shop": 2}
    global_options = {"pick nose": "don't pick your nose"}

    # print(main.testvar)
    # main.testvar = 2
    # print(main.testvar)
    # main.testvar = 3
    # print(os.environ.get('VAR'))
    # os.environ['VAR'] = "3"
    # print(os.environ.get('VAR'))
    # os.environ['VAR'] = "4"



    print("You wake up...What do you do?")
    option = input()
    #
    # print("what is your name")
    # variables.name = input()
    #
    # print(variables.name)
    # print(variables.age)

    # print(main.class_test.age)
    # main.class_test.age = 5
    # print(main.class_test.age)

    # print(variables.ages)
    # variables.ages = 5
    # print(variables.ages)
    # print("HELLO")


    for key in wake_up_options:
        if option in wake_up_options:
            option = wake_up_options[option]
            break
        else:
            option = 4

    while option != 0:
        if option == 1:
            print("You look around the room and see WALLS")
        elif option == 2:
            print("You leave the bedroom and continue on your way.")
            return 2
        elif option == 4:
            print("You can't do that!!")

        print("What do you do?")
        option = input()

        for key in wake_up_options:
            if option in wake_up_options:
                option = wake_up_options[option]
                break
            else:
                option = 4
