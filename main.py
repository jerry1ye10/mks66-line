#Credit to Ivan Zhang from period 4 for helping me in person with the line algorithm and test cases
from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line( 250, -250, 250, 250, screen, color)#vertical line
draw_line( -250, 250, 250, 250, screen, color)#horizontal line

draw_line( 0, 0, 1000, 250, screen, color)
draw_line( 0, 0, 1000, 500, screen, color)


draw_line( 0, 0, 250, 1000, screen, color)
draw_line( 0, 0, 500, 1000, screen, color)

draw_line( 0, 500, 250,0, screen, color)
draw_line( 250, 500, 500,100, screen, color)


draw_line( 250, 500, 500, 0, screen, color)
draw_line( 0, 400, 500, 0, screen, color)


display(screen)
save_extension(screen, 'img.png')
