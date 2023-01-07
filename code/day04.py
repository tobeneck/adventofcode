'''
Day 4 of Advent of Code 2022.
https://adventofcode.com/2022/day/4
'''

cleaning_plan = open("../data/day04.txt").readlines()
cleaning_plan = [elve_team.replace("\n", "") for elve_team in cleaning_plan]

count_fully_contained = 0
count_overlapping = 0
for elve_team in cleaning_plan:
    #get the start and end points for the two sections
    sections = elve_team.replace("-",",").split(",")
    sec_1_start = int(sections[0])
    sec_1_end   = int(sections[1])
    sec_2_start = int(sections[2])
    sec_2_end   = int(sections[3])

    #check if they are fully contained (and therefore overlapping):
    if ( (sec_1_start <= sec_2_start and sec_2_end <= sec_1_end) 
      or (sec_2_start <= sec_1_start and sec_1_end <= sec_2_end) ):
        count_fully_contained += 1
        count_overlapping += 1
    #If not check if they at least partially overlap:
    elif ( (sec_1_start <= sec_2_start and sec_2_start <= sec_1_end) 
        or (sec_2_start <= sec_1_start and sec_1_start <= sec_2_end) ):
        count_overlapping += 1

print("Task 1:", count_fully_contained)
print("Task 2:", count_overlapping)