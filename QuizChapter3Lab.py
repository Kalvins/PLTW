                                                                #Calvin Hua 






#Quiz is run by using the green run file button
#Global variable points inorder to keep track of score
points = 0
#input command asks a question and allows the user to answer it
answer =raw_input('How many eggs are in a dozen of eggs?')
if answer =='12'or answer =='twelve':
        print 'correct' 
        points = points + 1
#else command is added to decrease the possible bugs
else: 
    print 'wrong'
#print blank is used to create a line between each question/answer
print ' '

#raw_input is used because the answer is text
print 'What is the capital of California?'
Capital = raw_input()
if Capital == 'Sacramento' or Capital == 'sacramento':
        print 'You sure know your capitals'
        points = points + 1
#else is used again to prevent bugs
else: 
    print 'wrong The capital of California is Sacramento'
#print blank is used to create a line between each question/answer
print ' '

#print command is used to list out selections 
#before allowing the user to answer it
print 'Brad just got hurt should he..'
print 'A. Call for help'
print 'B. Sit there'
print 'C. Die...'
ABC =raw_input()
if ABC == 'A' or ABC == 'a' :
    print 'You\'re right'
    points = points + 1
#elif is used to add humor and also other selections
elif ABC == 'B' or ABC == 'b':
    print 'Really this is not going to save you'
elif ABC == 'C' or ABC == 'c':
    print 'You just got a small scratch and now you\'re going to die'
#again else command is used
else: 
    print 'Error you didn\'t pick any of them '
#print blank is used to create a line between each question/answer
print ' '

print 'What is the name of the dragon in \"Eragon\"?'
Eragon = raw_input ()
#order of the selection doesn't matter as seen below
#(the wrong answer is used first instead of the right)
if Eragon == "Eragon" or Eragon == "eragon" :
        print 'Wrong, guess you didn\'t read the book'
elif Eragon == 'Saphira' or Eragon == 'saphira' :
    print 'You\'re right, hopefully you didn\'t google it'
    points = points + 1
else: 
    print 'Wrong The main character of the book was Eragon but the dragon was Saphira'
#print blank is used to create a line between each question/answer
print ' '

america_question = raw_input('When was the War of 1812?')
if america_question == '1812'or america_question =='nineteenth century':
        print 'Slow Clap'
        points = points + 1
else: 
    print 'wrong you either didn\'t get the joke or you actually don\'t know'
print ' '

#Finally the points system collects the global variable 'points'
print 'Congratulations, you got',
#prints the amount correct
print points,
print 'answer right.'
print 'That is a score of',
#Then calculates the percentage right using points
print (points/5.00)*100,
print ' percent.'
