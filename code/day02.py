'''
Day 2 of Advent of Code 2022.
https://adventofcode.com/2022/day/2
'''

def calc_my_matchup_score_task_1(matchup):
    '''
    Calculates my score depending on my matchup choice and if I win against the enemy.
    The matchup is a string containing two characters, the first representing the choice of my enemy and the second representing my choice. The two characters are separated by a space.
    
    Enemy choice:
    A: Rock
    B: Paper
    C: Scissors

    My choices:
    X: Rock
    Y: Paper
    Z: Scissors

    Points are appointed both for a win or draw, as well as my choice:
    Choice points:
    Rock:       1 point
    Paper:      2 points
    Scissors:   3 points

    Matchup points:
    loose:      0 points
    draw:       3 points
    win:        6 points
    '''
    my_score = 0

    #add the point(s) for my choice
    if "X" in matchup:
        my_score += 1
    elif "Y" in matchup:
        my_score += 2
    elif "Z" in matchup:
        my_score += 3

    #add the points for the game result
    if ( #draw:
        matchup == "A X"    #both Rock
        or matchup == "B Y" #both Paper
        or matchup == "C Z" #both Scissor
    ): 
        my_score += 3
    elif ( #I win (yea!):
        matchup == "A Y"    #enemy: Rock     , me: Paper
        or matchup == "B Z" #enemy: Paper    , me: Scissors
        or matchup == "C X" #enemy: Scissors , me: Rock
        ): 
        my_score += 6

    return my_score

def calc_my_matchup_score_task_2(matchup):
    '''
    Calculates my score depending on my matchup choice and if I win against the enemy.
    The matchup is a string containing two characters. The first is representing the enemys choice, the second one if I loose the match or not. The characters are separated by a space.
    
    Enemy choice:
    A: Rock
    B: Paper
    C: Scissors

    Game result:
    X: loose
    Y: draw
    Z: win

    Points are appointed both for a win or draw, as well as my choice:

    Choice points:
    Rock:       1 point
    Paper:      2 points
    Scissors:   3 points

    Matchup points:
    loose:      0 points
    draw:       3 points
    win:        6 points
    '''
    my_score = 0

    #add the points for the game result
    if "Y" in matchup: #draw
        my_score += 3
    elif "Z" in matchup: #win
        my_score += 6

    #add the points for my choice
    if ( #I need to Rock (yea!):
        matchup == "A Y"    #enemy: Rock        , draw
        or matchup == "B X" #enemy: Paper       , loose
        or matchup == "C Z" #enemy: Scissory    , win
    ): 
        my_score += 1
    elif ( #I need to play Paper:
        matchup == "A Z"    #enemy: Rock        , win
        or matchup == "B Y" #enemy: Paper       , draw
        or matchup == "C X" #enemy: Scissory    , loose
        ): 
        my_score += 2
    elif ( #I need to play Scissors:
        matchup == "A X"    #enemy: Rock        , loose
        or matchup == "B Z" #enemy: Paper       , win
        or matchup == "C Y" #enemy: Scisory     , draw
        ): 
        my_score += 3

    return my_score



matchups_file = open("../data/day02.txt")
matchups_string = matchups_file.readlines()
matchups_string = [data.replace("\n", "") for data in matchups_string]

my_task_1_scores = [calc_my_matchup_score_task_1(data) for data in matchups_string]
print("Task 1: My overall tournament score if I use the strategy guide would be "+str( sum(my_task_1_scores) )+".")

my_task_2_scores = [calc_my_matchup_score_task_2(data) for data in matchups_string]
print("Task 2: My overall tournament score if I use the ultra top secret strategy guide would be "+str( sum(my_task_2_scores) )+".")