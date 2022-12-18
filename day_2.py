#!/usr/bin/env python

score = 0
rock = {"A", "X"}
paper = {"B", "Y"}
scissor = {"C", "Z"}

with open("./data.txt", "r") as file:
    data = file.read().splitlines()

#subset = data[:5]

for _ in range(len(data)):
    data[_] = data[_].split(" ")
    #print(f"subset[_] = {data[_]} originally...")
    for hand in range(len(data[_])):
        if data[_][hand] in rock:
            data[_][hand] = "rock"
        elif data[_][hand] in paper:
            data[_][hand] = "paper"
        elif data[_][hand] in scissor:
            data[_][hand] = "scissor"
    #print(f"And now it equals {data[_]}!")

for opp, me in data:
    # Determining score for hand played
    if me == "rock":
        score += 1
    elif me == "paper":
        score += 2
    elif me == "scissor":
        score += 3

    # Determininig match winner
    if opp == me:
        print("You tied!")
        score += 3
    elif opp == "rock":
        if me == "paper":
            print("Gottem!")
            score += 6
        elif me == "scissor":
            print("Ouch!")
            score += 0
    elif opp == "paper":
        if me == "rock":
            print("Ouch!")
            score += 0
        elif me == "scissor":
            print("Gottem!")
            score += 6
    elif opp == "scissor":
        if me == "rock":
            print("Gottem!")
            score += 6
        elif me == "paper":
            print("Ouch!")
            score += 0

print(f"score = {score}")