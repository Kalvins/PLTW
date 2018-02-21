def print_areas(room_widths): 
    ''' room_widths is a list of numeric values
    Prints groom areas of square rooms.
 
    Returns the last width.
    ''' 
    #start of the loop using a phrase and adding in numbers#
    print 'All rooms are square.'
    for width in room_widths:
    #shows the setup of the phrases#
        print 'Room area is ',
        print width**2
    print 'A very square house.'
    return width
    #answer#
def print_eggs(numbers_of_dozens): 
    '''numbers_of_dozens is a list of numeric values
    Prints the number of eggs in each number of dozens.
    Also prints "There are 12 eggs per dozen."
 
    Returns a str stating the number of values in numbers_of_dozens.
    ''' 
    for number in numbers_of_dozens:
    #giving the full amount of dozens and the amount of eggs for that amount of dozens#
        print number,
        print 'dozen contains ',
        print number*12,
        print 'eggs.'
    return 'That\'s ' + str(len(numbers_of_dozens))+ ' groups of dozens.'
    #Answer#
def number_of_eggs(dozens):
    #defines global variable#
    number_of_eggs = 0
    for number in dozens:
            number_of_eggs = (number_of_eggs) + (number)*12
            #starts the equation to determine number of eggs#
    return number_of_eggs    
    #answer#


def sum_area(room_widths): 
    ''' room_widths is a list of numeric values
    The shape of each room is square.
    
    Returns the total area of the rooms.
    ''' 
    #defines global variable (total_area)
    total_area = 0
    for width in room_widths:
    #shows the equation to determine total_area#
        total_area = total_area + width**2
    return total_area
    #answer#
def points(word): 
    '''word is a str
    The function calculates the points for a word based on
    a=1 point, b=2 points, ..., z=26 points

    Returns an int for the total points
    '''
    # defines global variable#
    points = 0
    for letter in word:
        ord(letter)-96,
        #grading system#
        points = points + ord(letter)-96
    # Then the answer#
    return points
def to_inches(heights): 
    '''heights is a list of numeric values measured in feet
    
    Returns a list of the measurements in inches.
    ''' 
    # defines the global variable (to inches)
    to_inches = []
    for height in heights:
        # shows how to convert height in feet to inches#
        to_inches.append(height*12)
    return to_inches
    # gives answer#

def word_lengths(phrase):
    #define the global variables for the repeating code#
    word_lengths = []
    count = 0
    words = phrase.split(' ')
    #selects the individual words and repeats the code#
    for word in words:
    #finds the lengths of the word#
        count=len(word)
    
        word_lengths.append(count)
    return word_lengths
    #gives the word lengths#
    
