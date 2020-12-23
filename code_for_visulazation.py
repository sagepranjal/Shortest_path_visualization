#import libraries

import pygame
import math
import numpy
from queue import PriorityQueueṣ


#difining the width

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* path finding algorithm")

#colors for the points

# RED = (255, 0, 0)

RED = (144,238,144)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


#visualization tool

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows


    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color==RED

    def is_open(self):
        return self.color == GREEN

    def barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE


    def maake_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_start(self):
        self.color = ORANGE

    def make_barrier(self):
        self.color= BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE


    def draw(self,win):
        pygame.draw.rect(win, self.color,(self.x , self.y , self.width , self.width) )

    def update_neighbours(self,grid):
        pass

    def __lt__(self,other):
        return False

# Heuristiscs Function ( manhattan distance or L distance )

def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)


#making the grid

def make_grid(rows, width):
    width = int(width)
    rows = int(rows)
    gap = width//rows
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j, gap,rows)
            grid[i].append(spot)

    return grid


#drawing the grid lines

def draw_grid(win, rows, width):

    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0, i*gap), (width, i*gap))

    for j in range(rows):
        pygame.draw.line(win,GREY,(j* gap, 0), (j*gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for rows in grid:
        for spot in rows:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_click_pos(pos,rows, width):
    gap = width // rows
    y, x = pos

    row = y//gap
    col = x//gap

    return row, col


# --------  main function of the code    --------

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

# -------- run function -------

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
                # this is for left mouse click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                spot = grid[row][col]

                if not start:
                    start = spot
                    start.make_start

                elif not end:
                    end = spot
                    end.make_end()

                elif spot!= end and spot!= start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:    #this is for right mouse click
                pass



    pygame.quit()





main(WIN, WIDTH)
