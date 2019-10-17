#! /usr/bin/env python
# Time-stamp: <2019-03-09 09:43:09 christophe@pallier.org>

""" Display a square using [pygame](http://www.pygame.org).

For a quick introduction on drawing with pygame,
see <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>
"""
import pygame

# Colors are triplets containint RGB values
# (see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

W, H = 1000, 1000  # graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.

# open the window and fill it with white
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(WHITE)

# crée cercles
pygame.draw.circle(screen, BLACK, (W // 4, H // 4), 100, 0)
pygame.draw.circle(screen, BLACK, ((W // 4)*3, H // 4), 100, 0)
pygame.draw.circle(screen, BLACK, (W // 4, (H // 4)*3), 100, 0)
pygame.draw.circle(screen, BLACK, ((W // 4)*3, (H // 4)*3), 100, 0)







# Create a rectangle (see )<https://www.pygame.org/docs/ref/rect.html>)
width, height = 500, 500
left, top = (W - width) // 2, (H-height) // 2
myrect = pygame.Rect(left, top, width, height)
pygame.draw.rect(screen, WHITE, myrect)





# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "Kanisza.png")

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

