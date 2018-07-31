sides = ["Fries", "Asparagus", "Beans", "Rice", "Bread"]
main = ["Steak", "Tacos", "Enchiladas", "Spaghetti"]
desserts = ["Ice cream", "Cake", "Pizookie", "Cheesecake"]

response = input("Would you like to hear the menu? (Y/N)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(sides)-1)
        print(sides[aRandomIndex])
        bRandomIndex = randint(0, len(main)-1)
        print(main[aRandomIndex])
        cRandomIndex = randint(0, len(desserts)-1)
        print(desserts[aRandomIndex])
    else:
        print("{} is an invalid input.".format(response))
    response = input("Would you like to hear the menu?(Y N)")
