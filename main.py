from time import sleep
import random


# I write functions in PascalCase.
def PrintSleep(input):
    print(input)
    sleep(2)


def KaufeAugustin(items, money):
    while True:
        augustin = input("If you want to buy the newspaper for 3€ type: y," +
                         "if you want to give the homeless person " +
                         "50 Cent type: 50" +
                         "and if you want to walk away type: n.\n")
        if augustin.lower() == "y":
            PrintSleep("You bought an Augustin")
            money -= 3
            items.append("Augustin")
            return items, money
        elif augustin.lower() == "50":
            PrintSleep("You gave the homeless person 50 Cent.")
            money -= 0.5
            return items, money
        elif augustin.lower() == "n":
            PrintSleep("You kept your money.")
            return items, money
        else:
            print("Invalid input")


def Hunger(money, bought_food):
    food = ["Langos", "Flammkuchen", "Käsespätzle", "Bratwurst",
            "Brezel", "Raclettebrot", "Kartoffelpuffer"]
    food_prices = {
        "Langos": 5,
        "Flammkuchen": 9,
        "Käsespätzle": 9,
        "Bratwurst": 6,
        "Brezel": 4.5,
        "Raclettebrot": 5,
        "Kartoffelpuffer": 3
        }
    is_break = False
    random_index = random.randint(0, 6)
    PrintSleep(f"You are interested in the {food[random_index]}.")
    PrintSleep(f"""The price of the {food[random_index]} is
{food_prices[food[random_index]]}€""")
    while True:
        purchase = input("If you want to buy it, type y," +
                         "if you do not want to buy it, type n\n")
        if purchase.lower() == "y" and \
           money >= food_prices[food[random_index]]:
            print(f"You bought the {food[random_index]}.")
            money -= food_prices[food[random_index]]
            sleep(2)
            print(f"Your new capital is: {money}€")
            sleep(2)
            if not bought_food:
                print("Now you are not hungry anymore.")
                bought_food = True
            return money, is_break, bought_food
        elif (purchase.lower() == "y" and
                money < food_prices[food[random_index]]):
            PrintSleep("You are sad," +
                       "because you can't afford to eat, what you wanted to.")
            PrintSleep("Therefore you go home.")
            is_break = True
            return money, is_break, bought_food
        elif purchase.lower() == "n":
            PrintSleep(f"You don't buy the {food[random_index]}.")
            return money, is_break, bought_food
        else:
            print("Invalid input")


def Thirst(money, bought_drink, promille):
    drinks = ["Tee", "Glühwein", "Punsch", "Kinderpunsch", "Kaffee", "Rum"]
    drink_prices = {
        "Tee": 2.5,
        "Glühwein": 3,
        "Punsch": 3,
        "Kinderpunsch": 3,
        "Kaffee": 3.5,
        "Rum": 5
        }
    is_drunk = False
    is_break = False
    random_items = random.sample(drinks, 3)
    PrintSleep(f"You are interested in the {random_items[0]}" +
               f" for {drink_prices[random_items[0]]}€," +
               f" the {random_items[1]} " +
               f"for{drink_prices[random_items[1]]}€ and the" +
               f" {random_items[2]} for" +
               f"{drink_prices[random_items[2]]}€")
    while True:
        purchase = input(f"""If you want the {random_items[0]}, type 0,
if you want the {random_items[1]}, type 1,
if you want the {random_items[2]}, type 2,
if you don't want a drink, type n'\n""")
        if purchase == "0":
            if money >= drink_prices[random_items[0]]:
                PrintSleep(f"You bought the {random_items[0]}.")
                money -= drink_prices[random_items[0]]
                PrintSleep(f"Your new capital is: {money}€")
                if random_items[0] == "Rum" or \
                   random_items[0] == "Glühwein" or \
                   random_items[0] == "Punsch":
                    promille += 1
                if not bought_drink:
                    PrintSleep("Now you are not thirsty anymore.")
                    bought_drink = True
            else:
                PrintSleep("You can't afford the drink.\n" +
                           "Therefore you go home.")
                is_break = True
            return money, is_break, bought_drink, promille
        elif purchase == "1":
            if money >= drink_prices[random_items[1]]:
                PrintSleep(f"You bought the {random_items[1]}.")
                money -= drink_prices[random_items[1]]
                PrintSleep(f"Your new capital is: {money}€")
                if random_items[1] == "Rum" or \
                   random_items[1] == "Glühwein" or \
                   random_items[1] == "Punsch":
                    promille += 1
                if not bought_drink:
                    PrintSleep("Now you are not thirsty anymore.")
                    bought_drink = True
            else:
                PrintSleep("You can't afford the drink.\n" +
                           "Therefore you go home.")
                is_break = True
            return money, is_break, bought_drink, promille
        elif purchase == "2":
            if money >= drink_prices[random_items[2]]:
                PrintSleep(f"You bought the {random_items[2]}.")
                money -= drink_prices[random_items[2]]
                PrintSleep(f"Your new capital is: {money}€")
                if random_items[2] == "Rum" or \
                   random_items[2] == "Glühwein" or \
                   random_items[2] == "Punsch":
                    promille += 1
                if not bought_drink:
                    PrintSleep("Now you are not thirsty anymore.")
                    bought_drink = True
            else:
                PrintSleep("You can't afford the drink.\n" +
                           "Therefore you go home.")
                is_break = True
            return money, is_break, bought_drink, promille
        elif purchase.lower() == "n":
            PrintSleep("You didn\'t buy a drink.")
            return money, is_break, bought_drink, promille
        else:
            print("invalid input")


def Anger(items, money, bought_toy):
    is_break = False
    toys = ["candle", "wooden jesus", "painted metall soldier"]
    toys_prices = {
        "candle": 3,
        "wooden jesus": 10,
        "painted metall soldier": 5
        }
    random_index = random.randint(0, 2)
    PrintSleep(f"You are interested in the {toys[random_index]}.")
    PrintSleep(f"The price of the {toys[random_index]} " +
               f"is {toys_prices[toys[random_index]]}€")
    while True:
        purchase = input(f"If you want to buy the {toys[random_index]}" +
                         "type y" +
                         ", if you do not want to buy it, enter n\n")
        if purchase.lower() == "y" and \
           money >= toys_prices[toys[random_index]]:
            PrintSleep(f"You bought the {toys[random_index]}.")
            items.append(toys[random_index])
            money -= toys_prices[toys[random_index]]
            PrintSleep(f"Your new capital is: {money}€")
            sleep(2)
            if not bought_toy:
                PrintSleep("Now you are not angry anymore.")
                bought_toy = True
            return items, money, is_break, bought_toy
        elif purchase.lower() == "y" and \
                money < toys_prices[toys[random_index]]:
            print("You are frustrated, " +
                  f"bacause you could not afford the {toys[random_index]}.")
            sleep(3)
            PrintSleep("Therefore you go home.")
            is_break = True
            return items, money, is_break, bought_toy
        elif purchase.lower() == "n":
            PrintSleep(f"You did not buy the {toys[random_index]}.")
            return items, money, is_break, bought_toy
        else:
            print("Invalid input")


def AdventureGame():
    items = []
    money = 18
    promille = 0
    bought_drink = False
    bought_food = False
    bought_toy = False
    PrintSleep("Welcome to the winter wonder land.")
    PrintSleep("You enter the christmas market.")
    PrintSleep('You encounter a homeless person who says:"Kaufe Augustin!"')
    items, money = KaufeAugustin(items, money)
    PrintSleep("You are hungry, angry and thirsty.")
    PrintSleep("Therefore you need something to drink," +
               " something to eat and a useless luxury product for joy.")
    PrintSleep(f"Your capital is {money}€.")
    PrintSleep("What do you want to do first?")
    PrintSleep("Look for food, get a drink, or buy a toy?")

    while True:
        action = input("""
In order to look for food, enter: hungry
In order to get a drink, enter: thirsty
In order to buy a toy, enter: angry
To go home, enter: ciao
""")
        if action.lower() == "hungry":
            money, is_break, bought_food = Hunger(money, bought_food)
            if is_break:
                break
        elif action.lower() == "thirsty":
            money, is_break, bought_drink, promille = \
                Thirst(money, bought_drink, promille)
            if is_break:
                break
        elif action.lower() == "angry":
            items, money, is_break, bought_toy = \
                Anger(items, money, bought_toy)
            if is_break:
                break
        elif action.lower() == "ciao":
            PrintSleep("You do not want to continue.")
            PrintSleep("Therefore you go home.")
            break
        else:
            print("invalid input")
        if promille > 2:
            PrintSleep("You are drunk, therefore you go home.")
            break
        if money <= 2:
            PrintSleep("You don't have enough money left" +
                       " to buy anything, therefore you go home.")
            break
    PrintSleep(f"You leave the winter wonder land with: {items} and {money}€.")
    if not bought_drink:
        PrintSleep("You are still thirsty.")
    if not bought_food:
        PrintSleep("You are still hungry.")
    if not bought_toy:
        PrintSleep("You are still angry.")
    if "wooden jesus" in items:
        PrintSleep("You are super happy, because you bought the wooden jesus.")
    elif bought_drink and bought_food and bought_toy:
        PrintSleep("You are satisfied.")
    while True:
        new_game = input("Do you want to play again? \n" +
                         "If so, enter y and if you don't want to enter n\n")
        if new_game.lower() == "y":
            AdventureGame()
        elif new_game.lower() == "n":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    AdventureGame()
