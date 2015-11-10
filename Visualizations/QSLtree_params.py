import pygame, math
width = 550*2
height = 350*2
num_contacts = 9


pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()
 




def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - 40, depth - 1)
        drawTree(x2, y2, angle + 40, depth - 1)
 
def input(event):
    if event.type == pygame.QUIT:
        exit(0)
 
drawTree(width/2, height - 50, -90, num_contacts)


pygame.display.flip()

pygame.image.save(screen, "QSLtree_params.png")


while True:
    input(pygame.event.wait())