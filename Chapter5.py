PI = 3.141592653
import pygame
import math
BROWN    = ( 210, 105,  30)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   82, 111, 53)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kalvin's Cool Game")
done = False
clock =pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        if event.type == pygame.QUIT:
                done = True       
                
    screen.fill(WHITE)   
    pygame.draw.rect(screen, RED, [175, 200, 400, 150])    
    pygame.draw.polygon(screen, BROWN, [[375,100], [175,200], [575,200]])
    pygame.draw.rect(screen, BROWN, [325, 250, 70, 100])
    pygame.draw.rect(screen, BLUE, [475, 250, 50, 50])
    pygame.draw.line(screen, WHITE, [500,250], [500,300], 5)
    pygame.draw.line(screen, WHITE, [475,275], [525,275], 5)
    pygame.draw.line(screen, BLACK, [177,200], [177,75], 5)
    pygame.draw.rect(screen, BLUE, [75, 75, 100, 75])
    
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()
