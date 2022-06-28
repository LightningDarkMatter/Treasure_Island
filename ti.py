print("Welcome to Tresure Island!")
print("You are on a deserted island and you need to find the treasure.")
print("You can go to the left or right.")
turn1 = input("Which way do you go? ")
if turn1 == "left":
    print("You go left and you find a river")
    print("Do you want to swim across or wait for a boat?")
    turn2 = input("Which do you want to do? ")
    if turn2 == "wait":
        print("You wait for a boat and are taken across the river")
        print("You are now on the other side of the river")
        print("You find three doors - Red, Green and Blue")
        turn3 = input("Which door do you choose? ")
        if turn3 == "green":
            print("You go through the green door and find a treasure chest")
            print("You open the chest and find a treasure!")
            print("You win!")
        elif turn3 == "red":
            print("You go through the red door and fall in to a pit")
            print("You lose!")
        elif turn3 == "blue":
            print("You go through the blue door and get eaten by a bear")
            print("You lose!")
    else: # turn2 == "swim"
        print("You swim across the river and get eaten by a shark")
        print("You lose!")
else: # turn1 == "right"
    print("You go right and you find a cave")
    print("There is a dragon in the cave, it eats you!")
    print("You lose!")