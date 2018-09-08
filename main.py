import pygame
pygame.init()

winWidth = 640
winHeight = 480

win = pygame.display.set_mode((winWidth, winHeight))

pygame.display.set_caption("Game")

width = 50
height = 60
x = (winWidth/2)-(width/2)
y = (winHeight/2)-(height/2)
vel = 5
jump = 50

run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if y < winHeight-height:
        y += 5

    if keys[pygame.K_LEFT] and 0 < x:
        x -= vel
    if keys[pygame.K_RIGHT] and x < winWidth-width:
        x += vel
    if keys[pygame.K_DOWN] and y < winHeight-height:
        y += vel
    if keys[pygame.K_SPACE] and y == winHeight-height:
        y -= jump
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
