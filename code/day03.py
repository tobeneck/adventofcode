'''
Day 3 of Advent of Code 2022.
https://adventofcode.com/2022/day/3
'''


def get_item_priority(item):
    '''
    Returns the priority of an item.
    Items are prioritiesed as follows:
    a=1, b=2, ..., z=26,
    A=27, B=28, ..., Z=52

    Parameters:
    -----------
    item : string
        A one-character string that represents the item to be prioritiest.
    
    Returns:
    --------
    priority : int
        The priority of the item
    '''
    item_ord = ord(item)
    ord_correction = 96 if item.islower() else 38
    return item_ord - ord_correction

def get_resorting_priority(rucksack):
    '''
    This method returns the re-sorting priorities of the one item that is present in both compartments of the rucksack.

    Parameters:
    -----------
    rucksack : string
        A string where each item is represented by a character.
        The first half of the string is compartment stored in compartment one of the rucksack, the second half in compartment two.
    
    Returns:
    --------
    priority : int
        The priority of the matching item pair.
    '''
    
    #split the rucksack into compartments:
    compartment_size = int(len(rucksack)/2)
    compartment_one = rucksack[:compartment_size]
    compartment_two = rucksack[compartment_size:]

    #find the item that is present in both (only one per rucksack is):
    item_in_both = ''.join(set(compartment_one).intersection(compartment_two))

    #get the priority of the item:
    priority = get_item_priority(item_in_both)

    return priority


def get_team_approval_priority(rucksack_1, rucksack_2, rucksack_3):
    '''
    Returns the priority for the team of three elves (with the rucksacks 1 to 3) to get their approval sticker.
    Every team has exaclty one item that is equal across across all three rucksacks.

    Parameters:
    -----------
    rucksack_1 : string
        Rucksack of the first elf in the team.
    rucksack_2 : string
        Rucksack of the second elf in the team.
    rucksack_3 : string
        Rucksack of the third elf in the team.
    
    Returns:
    --------
    priority : int
        The priority of the team to get their approval sticker.    
    '''
    #get the item that is present in all three rucksäcke (only one per rucksack is):
    team_item = ''.join(set(rucksack_1).intersection(rucksack_2).intersection(rucksack_3)) #TODO: can I do this nicer?

    #get priority for that item:
    team_sticker_priority = get_item_priority(team_item)

    return team_sticker_priority





rucksacks = open("../data/day03.txt").readlines()
rucksacks = [data.replace("\n", "") for data in rucksacks]

resorting_priorities = [ get_resorting_priority(rucksack) for rucksack in rucksacks]
print("Task 1:", sum(resorting_priorities))

sticker_attatchment_priorities = [ #3 elves form a team
    get_team_approval_priority(rucksacks[i], rucksacks[i+1], rucksacks[i+2]) for i in range(0, len(rucksacks), 3)
    ]
print("Task 2:", sum(sticker_attatchment_priorities))