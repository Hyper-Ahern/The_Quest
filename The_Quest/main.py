# USE THE SAME FORMAT AS I HAVE HERE AND THEN WHEN YOU WANT TO EXIT TO A NEW PLACE
# SIMPLY USE exit() CODE IN THE OTHER PAGE WITH A NUMBER INSIDE THE PARENTHESIS

import subprocess

adventure = 1

while adventure != 0:

    # your bedroom
    if adventure == 1:
        adventure = subprocess.call(['python', 'your_home/your_bedroom.py'])

    # your hallway
    elif adventure == 2:
        adventure = subprocess.call(['python', 'your_home/your_hallway.py'])

    # bob's item shop
    elif adventure == 3:
        adventure = subprocess.call(['python', 'shop.py'])

    # insert new area
    elif adventure == 4:
        print("THIS IS A PLACEHOLDER")

    # insert new area
    elif adventure == 5:
        print("THIS IS A PLACEHOLDER")

print("GAMEOVER")
