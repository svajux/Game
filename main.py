from collada import *

import pygame


class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def update(self,dt,key):
        s= dt*10

        if key[pygame.K_q]: self.pos[0] -= s
        if key[pygame.K_e]: self.pos[0] += s

        if key[pygame.K_w]: self.pos[2] += s
        if key[pygame.K_s]: self.pos[2] -= s
        if key[pygame.K_d]: self.pos[0] += s
        if key[pygame.K_a]: self.pos[0] -= s

pygame.init()

winWidth = 600
winHeight = 600
cWidth = winWidth/2
cHeight = winHeight/2
clock= pygame.time.Clock()
mesh = Collada('model.dae')
geom = mesh.geometries[0]
triSet = geom.primitives[0]
size = 100
offset = 250
win = pygame.display.set_mode((winWidth, winHeight))

pygame.display.set_caption("Game")

verts = (-1,1,-1),(-1,1,1),(1,1,1),(1,1,-1),(-1,-1,-1),(-1,-1,1),(1,-1,1),(1,-1,-1)
edges = (0,1),(2,3),(4,5),(6,7),(1,2),(3,0),(5,6),(7,4),(0,4),(1,5),(2,6),(3,7)
triVerts = []



triEdges = (0,1), (1,2), (2,0)

cam= Cam((0,0,-5))

run = True

while run:
    dt = clock.tick()/1000
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    triPoints = []
    for i in range(len(triSet.vertex[triSet.vertex_index])):
        x = triSet.vertex[triSet.vertex_index][i][0][0]
        y = triSet.vertex[triSet.vertex_index][i][0][1]
        z = triSet.vertex[triSet.vertex_index][i][0][2]
        x -= cam.pos[0]
        y -= cam.pos[1]
        z -= cam.pos[2]
        f = (winWidth / 2) / z
        x = x * f
        y = y * f
        vX = int((cWidth + x))
        vY = int((cHeight + y))
        triPoints += [(vX, vY)]

        print(triPoints[i])
        pygame.draw.polygon(win, (255,255,255), triPoints[i],0)




    for edge in edges:
        points = []
        for x, y, z in (verts[edge[0]], verts[edge[1]]):

            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
            f = (winWidth / 2) / z
            x = x * f
            y = y * f
            vX = int((cWidth + x))
            vY = int((cHeight + y))
            points += [(vX, vY)]

        pygame.draw.line(win, (255, 255, 255), points[0], points[1], 1)



    pygame.display.update()
    key = pygame.key.get_pressed()
    cam.update(dt,key)

pygame.quit()
