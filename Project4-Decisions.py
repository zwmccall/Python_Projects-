#Python script with inputs, string converters, function definitions, while bucle, if and else decisions

door = input("Choose a door: 1 or 2\n")

def add(one, two):
    return one + two

while(door != "2" or door != "1"):
    print(f"You've choosen door number {door}")
    if door == "1":
        print("There's a tiger behind the door.")
        print("What are you going to do?")
        beardecision = input("1. Hit the bear\n2. Run away\n")
        if beardecision == "1":
            print("Alright, you killed the bear and saved your life.")
        else:
            print("You cant' run from a bear, you're dead bruh.")
        break

    elif door == "2":
        print("There's a teacher behind the door.")
        print("He asks you to tell him your age")
        age = int(input(""))
        print("Now he want to know your weight")
        weight = int(input(""))
        print("Finally he asks you to tell him what is the sum of your age and weight")
        print("If you ")
        print("If you fail he will kill you")
        sum = int(input (""))
        correct = add(age, weight)
        print(f"The correct sum is {correct}")
        if (sum == correct):
            print("Congrats! Your're alive")
        else:
            print("You failed")
            print("The teacher hits you with his ruler till you die")
        break

    else:
        print("Bad choice")
        door = input("Choose a door: 1 or 2\n")
