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
    def __init__(self, color, col, row ):
        
        self.color = kolor
        self.row = row
        self.col = col


    def ruch(self, kierunek):
        if kierunek:
            self.col += 1
        else:
            self.col -= 1
        self.row+=1
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn   # Unpack the position
        dist_to_go = target_y - new_y_pos         # How far to our floor?

        if dist_to_go < 0:                        # Are we under floor?
            self.y_velocity = -0.65 * self.y_velocity     # Bounce
            new_y_pos = target_y + dist_to_go     # Move back above floor

        self.posn = (x, new_y_pos)   
    

def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255,255,255), (0,0,0)]    # Set up colors [red, black]

    n = 8         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.image.load("ball.jpg")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz-ball.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for row in range(3):
            for col in range(4):
                surface.blit(ball, ((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))

        for row in range(5,9):
            for col in range(4):
                surface.blit(ball, ((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2,0])    # 7 x 7 to test window size
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

