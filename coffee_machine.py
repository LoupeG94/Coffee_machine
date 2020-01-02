def buy(choice):
    global water
    global milk
    global coffee_beans
    global cups
    global money
    if is_enough(choice):
        print("I have enough resources, making you a coffee!")
        if choice == "1":
            water = water - 250
            coffee_beans -= 16
            cups -= 1
            money += 4
        elif choice == "2":
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7
        elif choice == "3":
            water -= 200
            milk -= 100
            coffee_beans -= 12
            cups -= 1
            money += 6
        elif choice == "back":
            main()


def fill():
    global water
    global milk
    global coffee_beans
    global cups

    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    print("The coffee machine has: ")
    water += add_water
    print(str(water) + " ml of water")
    milk += add_milk
    print(str(milk) + " ml of milk")
    coffee_beans += add_coffee_beans
    print(str(coffee_beans) + " gr of coffee beans")
    cups += add_cups
    print(str(cups) + " of disposable cups")
    print(str(money) + "$ of money")


def take():
    global money
    print("I gave you $" + str(money))
    money = 0


def remaining():
    print("The coffee machine has: ")
    print(str(water) + " ml of water")
    print(str(milk) + " ml of milk")
    print(str(coffee_beans) + " gr of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + "$ of money")


def is_enough(choice):
    if cups > 0:
        if choice == "1":
            if is_enough_water(250) and is_enough_coffee_beans(16):
                return True
            else:
                return False
        elif choice == "2":
            if is_enough_water(350) and is_enough_milk(75) and is_enough_coffee_beans(20):
                return True
            else:
                return False
        elif choice == "3":
            if is_enough_water(200) and is_enough_milk(100) and is_enough_coffee_beans(12):
                return True
            else:
                return False
    else:
        print("Sorry,not enough cups!")


def is_enough_water(required_water):
    if water - required_water >= 0:
        return True
    else:
        print("Sorry, not enough water !")


def is_enough_coffee_beans(required_coffee_beans):
    if coffee_beans - required_coffee_beans >= 0:
        return True
    else:
        print("Sorry, not enough coffee_beans!")


def is_enough_milk(required_milk):
    if milk - required_milk >= 0:
        return True
    else:
        print("Sorry, not enough milk!")


water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def main():
    while True:
        print("Write action (buy, fill, take, remaining, exit): ")
        action = str(input())
        if action == "buy":
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 'back' - main menu: ")
            buy(choice)
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "exit":
            break
        elif action == "remaining":
            remaining()
        else:
            print("Not recognised command !")


if __name__ == '__main__':
    main()
