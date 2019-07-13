# TEMPLATE FOR NEW PLACES
# Modify variables with main."variable here" = "value"
# Access variables with main."variable here"


def run():
    import main
    options = {"look around": 1, "look": 1, "check": 1, "leave": 2, "shop": 2}
    global_options = {"pick nose": "don't pick your nose"}

    print("You wake up...What do you do?")
    option = input()

    for key in options:
        if option in options:
            option = options[option]
            break
        else:
            option = 99

    while option != 0:
        if option == 1:
            print("You look.")
        elif option == 2:
            print("You leave.")
            return 2
        elif option == 99:
            print("You can't do that. Try something else.")

        print("What do you do?")
        option = input()

        for key in options:
            if option in options:
                option = options[option]
                break
            else:
                option = 99
