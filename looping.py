for row in range(10):
    print('*',end= ' ')
print (' ')
#------------------------------
for row in range(5):
    print ('*',end= ' ')
print (' ')
#---------------------------------
for row in range(20):
    print ('*',end= ' ')
print (' ')
#-------------------------------------
for row in range(10):
    for column in range(10):
        print ('*',end= ' ')
    print (' ')
#----------------------------------------
for row in range(10):
    for column in range(5):
        print ('*',end= ' ')
    print (' ')
#---------------------------------------------
for row in range(5):
    for column in range(20):
        print ('*',end= ' ')
    print (' ')
#--------------------------------------------
for row in range(10):
    for column in range(10):
        print (column,end= ' ')
    print (' ')
#------------------------------------
for row in range(10):
    for column in range(10):
        print (row,end= ' ')
    print (' ')
#--------------------------------------
for row in range(10):
    for column in range(row+1):
        print (column,end= ' ')
    print (' ')    
#---------------------------------------------------------
for row in range(1,9):
    for column in range(row+1):
        print (' ',end= ' ')
    for column in range(9-row):
        print (column,end=' ')
    print ()    
#--------------------------------------------------------------
for row in range(1,10):
    for column in range(1,10):
        if (column)*(row) < 10:
            print (' ',end='')
        print ((column)*(row),end=' ')
    print ()
#--------------------------------------------------------
for row in range(9):
    for column in range(9-row):
        print (' ',end=' ')
    for column in range(row+1):
        print ((1+column),end=" ")
    for column in range(row):
        if column <row:
            print ((row-column),end=' ')
        
    print()
#---------------------------------


for row in range(9):
    for column in range(9-row):
        print (' ',end=' ')
    for column in range(row+1):
        print ((1+column),end=" ")
    for column in range(row):
        if column <row:
            print ((row-column),end=' ')
    print () 
for row in range(10):
        for column in range(row+2):
            print (' ',end= ' ')
        for column in range(1,9-row):
            print (column,end=' ')
        print () 
print ()      
#------------------------------
for row in range(9):
    for column in range(9-row):
        print (' ',end=' ')
    for column in range(row+1):
        print ((1+column),end=" ")
    for column in range(row):
        if column <row:
            print ((row-column),end=' ')
    print () 
for row in range(9):
    for column in range(row+2):
        print (' ',end= ' ')         
    for column in range(1,9-row):
        print (column,end=' ')
    for column in range(7-row,0,-1):
            print (column,end=' ')
    print () 
print ()


        
        





