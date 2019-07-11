# Your Bedroom

wake_up_options = {"look around": 1, "look": 1, "check": 1, "leave": 2, "shop": 2}
global_options = {"pick nose": "don't pick your nose"}

print("You wake up...What do you do?")
option = input()

for key in wake_up_options:
    if option in wake_up_options:
        option = wake_up_options[option]

while option != 0:
    if option == 1:
        print("You look around the room and see WALLS")
    elif option == 2:
        print("You leave the bedroom and continue on your way.")
        exit(2)
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
