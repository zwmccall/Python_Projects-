import random

def get_guess():
    return list(input("What is Your Guess?"))

def generate_code():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)

    return digits[:3]

def generate_clues(code,user_guess):
    clues = []
    if user_guess == code:
        return "CODE CRACKED!"

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

print ("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()

    clue_report = generate_clues(secret_code,guess)
    print("here is the result of your guess:")
    for clue in clue_report:
        print(clue)
