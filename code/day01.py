'''
Day 1 of Advent of Code 2022.
https://adventofcode.com/2022/day/1
'''

calories_file = open("../data/day01.txt")

calorie_data = calories_file.readlines()

curr_elve = 0
elves = []

for line in calorie_data:
    curr_data = line.replace("\n", "")
    if curr_data == "":
        elves.append(curr_elve)
        curr_elve = 0
    else:
        curr_elve += int(curr_data)

print("The elf carrying the highest number of calories is carrying "+str( max(elves) )+" calories.")
print("The three elves carrying the highest number of calories are in total carrying "+str( sum(sorted(elves, reverse=True)[:3]) )+" calories.")




