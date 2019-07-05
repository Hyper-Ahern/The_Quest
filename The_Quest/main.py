# Bob's Item Shop

from items import Wallet
shop = {'Sword': 50, "Shield": 60, "Potion": 20}
shopOptions = {"Buy": 0, "Sell": 1, "Exit": 2}
masonWallet = Wallet()
masonWallet.currBalance += 100
print("Welcome to Bob's Item Emporium! How can I help you today fine traveller!")

print("Here are your options:")

for option in shopOptions:
        print(option)

state = input()

while state in shopOptions:
    operation = shopOptions[state]

    if operation == 0:
        for item, price in shop.items():
            print(item, ":", price)
        print('Exit')

        print("What would you like?")
        choice = input()

        while choice in shop:
            price = shop[choice]
            if masonWallet.currBalance >= price:
                masonWallet.currBalance -= price
                print("You have purchased", choice)
                print("You have", masonWallet.currBalance, "dollars remaining.")
                print("Would you like anything else?")
                for item, price in shop.items():
                    print(item + ":", price)
                print("Exit")
                choice = input()
            else:
                print("Im sorry, you don't have enough for that item.\nWas there anything else?")
                for item, price in shop.items():
                    print(item, ":", price)
                print('Exit')
                choice = input()
        if choice == "Exit":
            for option in shopOptions:
                print(option)
            state = input()

        else:
            print("I'm sorry we don't seem to have any", choice + ".")
            operation = 0

    elif operation == 1:
        print("Sorry we are not accepting items at this time\nPlease select another option.")
        for option in shopOptions:
            print(option)
        state = input()

    elif operation == 2:
        print("Thank you, have a spectacular day!")
        exit()

else:
    print("Oh dear, I'm afraid we don't do that here..\nWhat would you like to do?")
    for option in shopOptions:
        print(option)
    state = input()
# test