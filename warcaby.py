#class GameBoard(object):



#     plansza = [1, 2, 1, 2, 1, 2, 1, 2],
# [2, 1, 2, 1, 2, 1, 2, 1],
# [1, 2, 1, 2, 1, 2, 1, 2],
# [2, 1, 2, 1, 2, 1, 2, 1],
# [1, 2, 1, 2, 1, 2, 1, 2],
# [2, 1, 2, 1, 2, 1, 2, 1],
# [1, 2, 1, 2, 1, 2, 1, 2],
# [2, 1, 2, 1, 2, 1, 2, 1]


import pygame
class pionek(object):
    def __init__(self,img, pos):
        #pos to (row, col)
        self.img=img
        self.pos = pos


    def ruch(self, kierunek):
        pos=self.pos
        if kierunek:
            col = pos[0]+1 
        else:
            col = pos[0]-1
        row=pos[1]+1
        self.posn=(row,col)
        
    
    def draw(self, surface):
        surface.blit(self.image, self.posn)
    

def main()):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255,255,255), (0,0,0)]    # Set up colors [red, black]

    n = 8         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    
    player1=[]
    player2=[]
    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))
    ball = pygame.image.load("ball.jpg")    

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz-ball.get_width()) // 2
    for row in range(n):           # Draw each row of the board.
        c_indx = row % 2           # Alternate starting color
        for col in range(n):       # Run through cols drawing squares
            the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
            surface.fill(colors[c_indx], the_square)
            # Now flip the color index for the next square
            c_indx = (c_indx + 1) % 2
    for row in range(3):
        for col in range(4):
            pion=pionek(ball, (row,col))
            player1.append(pion)
            #((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))

    for row in range(5,9):
        for col in range(4):
            pion=pionek(ball, (row,col))
            player2.append(pion)
            #surface.blit(ball, ((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Draw a fresh background (a blank chess board)
       
        # Now that squares are drawn, draw the queens.
        for pion in player1+player2:
            pion.drow(surface)
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2,0])    # 7 x 7 to test window size
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

