# To simulate 1 game of Ezee, call game() .
# ezee.py implements all functions in ICS Project 2.2.6 
# (c) 2015 Project Lead The Way

import random 
def roll_die(): 
    ''' Return a random number 1-6
    ''' 
    return random.randint(1, 6)

def first_roll(): 
    ''' Return a list of n dice'''
    dice = []
    for i in range(14):
        dice.append(random.randint(1, 7))
    return dice




def reroll_one(dice, index): 
    ''' dice is a list of 14 numbers
    index is an int 0-13
    Return the list of dice, with a number randomly chosen from 1 to 6 to replace the item at index'''
    dice[index] = random.randint(1, 6)
    dice[index] = roll_die() # Either of these works.
    return dice



def count_frequency(dice, number): # Accumulator pattern
    ''' dice is a list of fourteen ints
    number is an int
    returns the frequency of the number among elements of dice
    '''
    frequency = 0 # Could use any variable name
    for die in dice: 
        if die == number: 
            frequency += 1
    return frequency
def biggest(number_list): 
    ''' return the biggest number in the number_list
    '''
    record = number_list[0] # Initialize record
    for number in number_list: 
        if number > record: # Record has been broken
            record = number # Set the new record
    return record 

def find_mode(dice): 
    ''' Accepts a list of numbers.
    Returns the most common number in the list.
    Returns one of the most common if there is a tie.
    '''
    record = 0 # Initialize record
    for number in [1, 2, 3, 4, 5, 6]:
        if count_frequency(dice, number) > record: # Record broken
            record = count_frequency(dice, number)# Set the new record
            record_holder = number
    return record_holder
def list_unmatched_dice(dice, target): 
    '''Accepts dice    ::a list of numbers.
               target  ::a number
    Returns the indicies of dice where the die does not match target
    '''
    unmatched = []
    for index in range(14):
        if dice[index] != target:
            unmatched.append(index)
    return unmatched 
def reroll_all_auto(dice):
    '''Accepts a list of 14 dice. 
    Find the mode and reroll the other dice. 
    Return the rerolled dice.  
    '''
    mode = find_mode(dice)
    dice_to_reroll = list_unmatched_dice(dice, mode)
    for index in dice_to_reroll:
        dice = reroll_one(dice, index) # Assignment unnecessary
    return dice
def won(dice): 
    '''dice is a list of 14 ints 1-6
    checks for 14 of a kind
    returns True or False
    '''
    if dice == [dice[0]]*14:
        match = True
    else:
        match = False
    return match
def game(debug=False): 
    '''rolls 14 dice and repeats until getting an Ezee
    returns the number of rolls made.
    '''
    dice = first_roll()
    counter = 1
    if debug:
        print dice
    while not won(dice):
        counter += 1
        reroll_all_auto(dice)
        if debug:
            print dice
    return counter