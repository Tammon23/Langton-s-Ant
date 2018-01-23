# Rules of Langton's Ant
#   1. If the ant is on a black square, it turns
#       right 90 and moves forward one unit
#   2. If the ant is on a white square, it turns
#       left 90 and moves forward one unit
#   3. When the ant leaves a square, it inverts
#       colour

# #Ikenna
from pygame.locals import *
from random import randint
import pygame

dirs = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
        )

board = [] # the list that will be holding weather or not the ant has been at a spot
cellSize = 6 # the size in pixels of the board (4 pixels are used to draw the grid)
numCells = 160 # length of the side of the board
backgroundClr = 0, 0, 0
gridClr = backgroundClr #0, 255, 0 # -- Bright green; colour of the grid
colours = [(0, 0, 0), (255, 255, 255)] # first tuple is the background colour, the second tuple is the ant's trail
antant = 0, 0, 255 # the ant's colour
fps = 100000# the amout of frames that will be shown per second, adjusts the speed of the ant's movement
CLOCK = pygame.time.Clock() # used for that ^^^ (the fps)

def main():
    pygame.init()

    size = numCells * cellSize, numCells * cellSize

    pygame.display.set_caption("Ikennas's version of Langton's Ant ")

    screen = pygame.display.set_mode(size) # Screen is now an object representing the window in which we paint
    screen.fill(backgroundClr)
    pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called

    for pos in range(1, numCells):
        pygame.draw.line(screen, gridClr, (pos * cellSize, 1), (pos * cellSize, numCells * cellSize), 1)
        pygame.draw.line(screen, gridClr, (1, pos * cellSize), (numCells * cellSize, pos * cellSize), 1)
    pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called

    font = pygame.font.Font(None, 36)

    antx, anty = numCells / 2, numCells / 2
    antdir = 0

    # generating the board
    for cell in range(numCells):
        tempList = [1] * numCells
        board.append(tempList)


    step = 1
    while True:
        pygame.event.pump()
        k = pygame.key.get_pressed()
        if k[pygame.K_q] or k[pygame.K_ESCAPE]:
            break

        if board[int(antx)][int(anty)] % 2 == 0: # if the number is even means ant should turn 90 degrees right
            board[int(antx)][int(anty)] = board[int(antx)][int(anty)] + 1  # See rule 3
            screen.fill(colours[0], pygame.Rect(antx * cellSize + 1, anty * cellSize + 1, cellSize - 1, cellSize - 1))
            antdir = (antdir + 1) % 4
        else:
            board[int(antx)][int(anty)] = board[int(antx)][int(anty)] + 1
            screen.fill(colours[board[int(antx)][int(anty)] - 1], pygame.Rect(antx * cellSize + 1, anty * cellSize + 1, cellSize - 1, cellSize - 1))
            antdir = (antdir + 3) % 4

        # the highest amount of transformatiosn the ant has done
        highTrans = 1
        # if we need a new colour for the ant make one
        if board[int(antx)][int(anty)] > highTrans:
            newClr = (randint(0, 255), randint(0, 255), randint(0, 255))
            colours.append(newClr)
            highTrans = board[int(antx)][int(anty)]

        antx = (antx + dirs[antdir][0]) % numCells
        anty = (anty + dirs[antdir][1]) % numCells

        # The current square the ant is on is painted a different colour,
        screen.fill(antant, pygame.Rect(antx * cellSize + 1, anty * cellSize + 1, cellSize - 1, cellSize -1))

        pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called

        step += 1
        CLOCK.tick(10)
    pygame.quit(    )
    print("Greatest number of transformations -", highTrans)
    print("Total number of steps performed -", step)

if __name__ == "__main__":
    main()