import pygame
import numpy as np
import time

#Initialize all modules imported from pygame
pygame.init()
#Screen width and height
width, heigth = 650, 650
#Creation of the screen
screen = pygame.display.set_mode((heigth, width))
#Background color = almost black, almost dark
bg = 25, 25, 25
#Paint the background with the chosen color
screen.fill(bg)

#Number of cells
nxC, nyC = 40, 40
#Cell dimensions
dimCW = width  / nxC
dimCH = heigth / nyC
#Cell status: alive = 1, dead = 0
gameState = np.zeros((nxC, nyC))

#Game execution control
pauseExect = True

running = True

#Execution loop
while running:
    #Copy current game state
    newGameState = np.copy(gameState)
    #Clean the screen
    screen.fill(bg)
    #Delay of 0.1s
    time.sleep(0.1)

    #Log keyboard and mouse events
    ev = pygame.event.get()
    for event in ev:
        #Detect if a key is pressed
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        #Close the game
        if event.type == pygame.QUIT:
            running = not running
        #Detect if mouse is pressed
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    #Get events from the queue
    pygame.event.get()
    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
                #Calculate the number of closest neighbors
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x)     % nxC, (y - 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x - 1) % nxC, (y)     % nyC] + \
                        gameState[(x + 1) % nxC, (y)     % nyC] + \
                        gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                        gameState[(x)     % nxC, (y + 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y + 1) %nyC]
                #Rule 1: a dead cell with exactly 3 live neighbors "revives"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                #Rule 2: A living cell with less than 2 or more than 3 living neighbors "dies."
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
            #Create the polygon of each cell to draw
            poly = [
                    ((x)     * dimCW,  y * dimCH),
                    ((x + 1) * dimCW,  y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x)     * dimCW, (y + 1) * dimCH)
                    ]
            #Draw the cells for each pair of x and y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    #Update game status
    gameState = np.copy(newGameState)
    #Refresh screen
    pygame.display.flip()