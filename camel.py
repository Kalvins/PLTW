                                                            #Calvin Hua


#imports the system function to exit the game
import sys
#imports the random function for the random chance from each command
import random
#[Intro text] into the game sets the back story for the game
print  'Welcome to Camel!'
print 'You have stolen a camel to make your way across the great Mobi desert.'
print 'The natives want their camel back and are chasing you down! Survive your'
print 'desert trek and out run the natives.'
#Boolean variable to end the game 
done = False 
#Values such as the miles traveled
Miles = 0
#Drinks left in Canteen
Drinks  = 6
#Natives distance from you
Natives  = -20
#Camel Tireness
Camel = 0
#Thirst Meter 
Thirst = 0
#Distance between you and the Natives calculated
Distance_between_you_and_the_Natives = 20
#Distance in which you are at the end of the game
End_game = 100
#If the player/camel dies or you end the game it runs this function to end
if done == True:
#exits the game
    sys.exit()
#repeating function for each choice 
while not done:
#list of choices that you can pick
    print 'A. Drink from your canteen.'
    print 'B. Ahead moderate speed.'
    print'C. Ahead full speed.'
    print'D. Stop for the night.'
    print'E. Status check.'
    print'Q. Quit.'
#function to allow you to input a choice
    answer = raw_input()
#function A allows you to drink from your canteen and checks/tells you how much 
#water you have
    if answer == 'A' or answer == 'a':
#Checks if there are drinks left
        if Drinks == 0:
            print 'No water' 
#Resets Thirst and subtracts one drink
        if  Drinks > 0:
            Thirst = 0
            Drinks = Drinks - 1
            print 'There is',
            print(Drinks),
            print'Drinks left'
        
    if answer == 'B' or answer == 'b':
        print 'You steadily ride away'
#Increase the Camel's tireness by 2
        Camel = Camel + 2
#You move 4-6 miles
        Miles = Miles + random.randint(4,6)
#Natives get closer by 2-5 miles
        Natives = Natives + random.randint(2,5)
#Thirst is increased by 2-4
        Thirst = Thirst + random.randint(2,4)
#Calculates the Distance between you and the Natives
        Distance_between_you_and_the_Natives = Miles - Natives
        
        if random.randint(1,20) == 20:
            Drinks = 6
            print 'You found an oasis'
    if answer == 'C' or answer == 'c':
        print 'You sprint away as fast as you can go'
#Increase the Camel's tireness by 3
        Camel = Camel + 3
#You move 6-10 miles
        Miles = Miles + random.randint(6,10)
#Natives get closer by 5-8 miles
        Natives = Natives + random.randint(5,8)
#Thirst is increased by 4-6
        Thirst = Thirst + random.randint(4,6)
#Calculates the Distance between you and the Natives
        Distance_between_you_and_the_Natives = Miles - Natives
#If you find an oasis (1-6 chance) your canteen is filled and you have 6 drinks
        if random.randint(1,10) == 10:
            Drinks = 6
            print'You found an oasis'
    if answer == 'D' or answer == 'd':
        print 'The Camel thanks you'
#The Camel rests and its tireness meter is reset.
        Camel = 0
#Natives get closer by 7-9 miles
        Natives = Natives + random.randint(7,9)
#Thirst is increased by 1-3
        Thirst = Thirst + random.randint(1,3)
#Calculates the Distance between you and the Natives
        Distance_between_you_and_the_Natives = Miles - Natives
    if answer == 'E' or answer == 'e':
#prints the drinks left, Camel Tireness meter, miles traveled, distance from natives       
        print 'You check your supplies'
        print 'Miles traveled',(Miles) 
        print 'Drinks left',(Drinks)
        print 'Distance away from Natives',(Distance_between_you_and_the_Natives)
        print  'Camel\'s Tireness',(Camel)
#The natives get closer by 2 miles
        Natives = Natives + 2
        
        print 'The Natives got closer while you were checking your supplies'
#if you travel to 50 miles you are 50 miles away from winning
    if Miles == 50 or Miles >50:
        print 'You are about to escape the Natives'
#if the Natives overtake you, you lose
    if Natives > Miles:
        print 'The Natives got you they took your camel and arrested you'
#Arrested as in killed
        done = True
#If the Natives are 15 miles behind you they are close
    if Distance_between_you_and_the_Natives == 15:
        print 'The Natives are close'        
#If your camel runs out of energy it dies
    if Camel > 10:
        print 'Your camel is dead'
        done = True
#Tells you that the camel is tired
    if Camel > 5:
        print 'Your camel grunts for rest'
#If you forget to drink water you die
    if Thirst > 10:
        print 'You died of thirst'
        done =True
#Tells you when you are thirsty
    if Thirst > 3:
        print 'You are thirsty'
        
#If you choose Q(q) you quit the game
    if answer == 'Q' or answer == 'q':
        print 'Thanks for playing Camel'
        done = True
#[End game text] When you escape the Natives the game ends with a message
    if Miles == End_game or Miles > End_game:
        print 'You won'
        print 'What you expected more?'
        print 'Have I not written enough code for you?!!?!!!?'
        done = True