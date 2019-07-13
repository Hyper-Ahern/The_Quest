# USE THE SAME FORMAT AS I HAVE HERE AND THEN WHEN YOU WANT TO EXIT TO A NEW PLACE
# SIMPLY USE exit() CODE IN THE OTHER PAGE WITH A NUMBER INSIDE THE PARENTHESIS

import subprocess
import variables
import os
import your_home.your_bedroom, your_home.your_hallway


adventure = 1

# testvar = 0
# # print(testvar)
# testvar = 1
# print(testvar)
# os.environ['VAR'] = "1"
# print(os.environ.get('VAR'))
# os.environ['VAR'] = "2"
# print(os.environ.get('VAR'))


# variables.initialize()
# print(variables.name)
# print(variables.age)
# variables.name = "joe"
# variables.age = 33
# print(variables.name)
# print(variables.age)
#
# variables.name = input()

# print("HELLLLOOOOO... please state your age")
# variables.age = input()
# print(variables.age)

# class_test = variables.Testing()
# class_test.age = 4
# print(class_test.age)

# variables.initialize()

# print(variables.ages)
# variables.ages = 99
# print(variables.ages)


while adventure != 0:
    # print(class_test.age)

    # your bedroom
    if adventure == 1:
        # adventure = subprocess.call(['python', 'your_home/your_bedroom.py'])
        adventure = your_home.your_bedroom.run()
        # print(testvar)

    # your hallway
    elif adventure == 2:
        # subprocess.call(['python', 'your_home/your_hallway.py'])
        adventure = your_home.your_hallway.run()
        # print(testvar)
        # print("hello")

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
