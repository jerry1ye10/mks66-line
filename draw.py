#Credit to Ivan Zhang from period 4 for helping me in person with the line algorithm and test cases
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = (y1 - y)
    B = -1 * (x1 - x)
    if(y <= y1):#Quadrants 1 and 3
        if(abs(A) <= abs(B)): #Octants 1 and 5 (same algorithm)
            D = (2 * A) +B
            while x <= x1:
                plot(screen, color, x, y)
                if D > 0:
                    y += 1
                    D += 2 * B
                D += 2 * A
                x += 1
        else: #Octants 2 and 6 (same algorithm)
            D = A + (2 * B)
            while y <= y1:
                plot(screen, color, x, y)
                if D < 0:
                    x+=1
                    D += 2 * A
                D += 2 * B
                y += 1
    else:#Quadrants 2 and 4; same algo
        if(abs(A) <= abs(B)):#Octants 4 and 8
            D = (2 * A) -B
            while x <= x1:
                plot(screen, color, x, y)
                if D < 0:
                    y -= 1
                    D -= 2 * B
                x += 1
                D += 2 * A
        else: #Octants 5 and 7; same algo
            D = A - (2 * B)
            while y >= y1:
                plot(screen, color, x, y)
                if D > 0:
                    x += 1
                    D += 2 * A
                y += -1
                D += -1 * (2 * B)
