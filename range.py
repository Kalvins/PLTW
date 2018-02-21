range(3)
def sequence(stop):
    number_list = []
    counter = 0
    while counter<stop:
        number_list.append(counter)
        counter = counter + 1
    return number_list
#calculate tax with the rate and amount
def add_tax(amount,tax_rate):
    tax_decimal= amount * tax_rate
    tax = tax_decimal + amount
    return tax(200.00, 0.05)
#roll a pair of dice and add them together
def roll_pair_of_dice():   
    import random 
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    pair_of_dice = dice1 + dice2
    return pair_of_dice
#find the mean of any 3 numbers
def mean (a,b,c):
    mean = (a+b+c)/3.0
    return mean
#find the hypotenuse of a triangle
def hypotenuse(leg1, leg2):
    leg11 = (2**leg1) + (2**leg2)
    hypotenuse = leg11**(1/2.0)
    return hypotenuse

