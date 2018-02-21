#Global Variables                                                                 Calvin Hua
a = 0
n= 3
#Creates a stairway like structure 
for row in range(10):
    for column in range(row):
#increases the number by 1 from the top down 
        a= a+1
        print ((a + 9),end=' ')
    print (' ')   
print ()
#-----------------------------------------------------------------
#requests for an input 
k = int(input('Box = '))
#prints two lines 
for i in range(k*2):
    print('o',end='')
print ()
for i in range(k):
    print('o',end='')
#prints the spaces according to the input
    for q in range(k*2-2):
        print(' ',end='')
    print('o')
    
#prints the final line
for i in range(k*2):
    print('o',end='')
    #-----------------------------------------------------------------
    x = -9
    y = -9
    import pygame
    import math
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    BLUE     = (   0,   0, 255)
    pygame.init()
    
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("My Game")
    
    done = False
    
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    
    
            screen.fill(BLACK)
    
#repeats the line of rectangle down each row    
    for a in range(100):
#changes the rectangles distance from left by 10 to the right
        y = y + 10
#sets the location of the first rectangle
        x = - 10
        for b in range(100):  
#prints a line of rectangles 
            x = x + 10
#prints a single rectangle
            pygame.draw.rect(screen, GREEN, [5+x, 5+y, 5, 5])
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()