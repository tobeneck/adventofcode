'''
Day 5 of Advent of Code 2022.
https://adventofcode.com/2022/day/5
'''


def parse_crate_moving_instructions(instructions):
    '''
    Parses the crate moving instructions string to the integers for amount to be moved, start stack and end stack.

    Parameters:
    -----------
    instructions : string
        The crate moving instruction string.

    Returns:
    --------
    list : [amount: int, start_stack: int, end_stack: int]
        A list witht the amount to be moved, the start stack and the end stack.
    '''
    instructions = instructions.replace("move ", "").replace("from ","").replace("to ","").split(" ")

    amount      = int( instructions[0] )
    start_stack = int( instructions[1] ) - 1
    end_stack   = int( instructions[2] ) - 1

    return [amount, start_stack, end_stack]



data = open("../data/day05.txt").readlines()
data = [elve_team.replace("\n", "") for elve_team in data]

split_element = data.index("")#above are the crate_stacks, below are the stacking instructions. The element itself is a empty row.

#parse the crate stacks:
number_of_stacks = int( [item for item in data[split_element-1].split(" ") if item != ""][-1] ) #reads the legend of the crate_stacks
crate_stacks = [[] for i in range(number_of_stacks)]
for line in data[:split_element-1]:
    for stack_index in range(number_of_stacks): 
        char_index = 1 + 4 * stack_index #Magic numbers. Every 4th element in the string holds an item, starting at index 1.
        char = line[char_index]
        if char != " ":
            crate_stacks[stack_index].insert(0, char)


#re-sort the stacks
crate_stacks_crate_mover_9000 = [stack.copy() for stack in crate_stacks]
crate_stacks_crate_mover_9001 = [stack.copy() for stack in crate_stacks]
for crane_movement_instructions in data[split_element+1:]:
    amount, from_stack, to_stack = parse_crate_moving_instructions(crane_movement_instructions)

    #use CrateMover 9000
    items_to_move = [ crate_stacks_crate_mover_9000[from_stack].pop() for i in range(amount)]
    crate_stacks_crate_mover_9000[to_stack] += items_to_move

    #use CrateMover 9001
    items_to_move = reversed( [ crate_stacks_crate_mover_9001[from_stack].pop() for i in range(amount)] )
    crate_stacks_crate_mover_9001[to_stack] += items_to_move

top_items_crate_mover_9000 = [stack[-1] for stack in crate_stacks_crate_mover_9000]
print("Taks 1:", "".join(top_items_crate_mover_9000))

top_items_crate_mover_9001 = [stack[-1] for stack in crate_stacks_crate_mover_9001]
print("Taks 2:", "".join(top_items_crate_mover_9001))