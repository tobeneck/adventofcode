'''
Day 6 of Advent of Code 2022.
https://adventofcode.com/2022/day/6
'''

def is_marker(chars):
    '''
    Checks if the given string of characters is a marker or not.
    It is a marker if no characters appear multiple times in a string.

    Parameters:
    -----------
    chars : string
        The set of characters to be checked.
    
    Returns:
    --------
    is_marker : boolean
        If the set of characters is a marker.
    '''
    for i in range(0, len(chars)):
        if chars.count(chars[i]) > 1:
            return False
    return True

datastream = open("../data/day06.txt").readline()

#package marker:
package_start_index = 0
package_marker_length = 4
while not is_marker(datastream[package_start_index:package_start_index+package_marker_length]): package_start_index += 1
print("Task 1:", package_start_index+package_marker_length)

#message marker:
message_start_index = package_start_index
message_marker_length = 14
while not is_marker(datastream[message_start_index:message_start_index+message_marker_length]): message_start_index += 1
print("Task 2:", message_start_index+message_marker_length)