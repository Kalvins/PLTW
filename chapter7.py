#creates a list for rooms 
room_list = []
#------------------------------------------------------------------------------------------------------------------------    
#adds every room listed into the list
#0
room = ['You are in a dark room. There is a door to the East',None,1,None,None]
room_list.append(room)
#1
room = ['You are in a big open area. There is a hallway to the North,East,West',3,2,None,0]
room_list.append(room)
#2
room = ['You are at a balcony and you look out. There is a door to the North,South,West',4,None,6,1]
room_list.append(room)
#3
room = ['You are in a bedroom likely own by a rich family. There is a door to the North,East,South',5,4,1,None]
room_list.append(room)
#4
room = ['You are in another bedroom it looks like it was connected. There is a passage to the South,West',None,None,2,3]
room_list.append(room)
#5
room = ['You are at what looks like a sniper perch. There is a passage to the South',None,None,3,None]
room_list.append(room)
#6
room = ['You are in a room There is a passage to the North',2,None,None,None]
room_list.append(room)
#------------------------------------------------------------------------------------------------------------------------    
#imports current_room and a boolean variable to quit
current_room = 0
done = False
#------------------------------------------------------------------------------------------------------------------------
#intro text into game 
print ('Welcome to Adventure')
start_input = input('Type y to start or n to exit, type i for instructions:')
print ()
#instructions to the game 
if start_input == 'i'or start_input == 'I':
    print ('type quit to exit the game at any time,type y to start the game')
    print ('type n, e, s, w according to the directions given to move')
if start_input == 'quit' or start_input =='n':
    print ('Bye')
    done = True
#------------------------------------------------------------------------------------------------------------------------    
#prints current room and asks where you want to go
while not done:
    print (room_list[current_room][0])
    print()
    user_input = input('Where do you go?:')
    
#------------------------------------------------------------------------------------------------------------------------
#tells the program what to do to go North    
    if user_input == 'n':
        next_room = room_list[current_room][1]
        if  next_room != None:
            current_room = next_room
        if next_room == None:
            print ('You can\'t go this way')    
#------------------------------------------------------------------------------------------------------------------------    
#tells the program what to do to go East
    if user_input == 'e':
        next_room = room_list[current_room][2]
        if  next_room != None:
            current_room = next_room
        if next_room == None:
            print ('You can\'t go this way')    
#------------------------------------------------------------------------------------------------------------------------       
#tells the program what to do to go South    
    if user_input == 's':
        next_room = room_list[current_room][3]
        if  next_room != None:
            current_room = next_room
        if next_room == None:
            print ('You can\'t go this way')   
#------------------------------------------------------------------------------------------------------------------------     
#tells the program what to do to go West    
    if user_input == 'w':
        next_room = room_list[current_room][4]
        if  next_room != None:
            current_room = next_room
        if next_room == None:
            print ('You can\'t go this way')   
#------------------------------------------------------------------------------------------------------------------------    
#allows you to quit the game
    if user_input == 'quit' or user_input == 'Quit':
        done = True
        print ('Your character jumps off the nearby balcony')
        print ('Thanks for playing')
#------------------------------------------------------------------------------------------------------------------------    
#if the user chooses anything other than the choices given this message is given
    if user_input != 'n'and user_input != 'e'and user_input != 's' and user_input != 'w' and user_input != 'quit'and user_input != 'Quit':
        print('That is not an option')