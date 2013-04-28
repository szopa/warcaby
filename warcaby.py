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
    def __init__(self,img, posn,img2):
        #pos to (row, col)
        self.image=img
        self.posn = posn
        self.img2=img2


    def ruch(self, kierunek):
        posn=self.posn
        if kierunek:
            col = posn[0]+1 
        else:
            col = posn[0]-1
        row=pos[1]+1
        self.posn=(row,col)
        
    
    def draw(self, surface):
        surface.blit(self.image, self.posn)
    
    def contains_point(self, pt):
      """ Return True if my sprite rectangle contains point pt """
      (my_x, my_y) = self.posn
      my_width = self.image.get_width()
      my_height = self.image.get_height()
      (x, y) = pt
      return ( x >= my_x and x < my_x + my_width and
               y >= my_y and y < my_y + my_height)
    
    def handle_click(self):
        self.img=self.image
        self.image = self.img2
    def handle_unclick(self):
        self.img2 = self.image
        self.image=self.img
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
    ball1 = pygame.image.load("ball1.jpg")
    ball2 = pygame.image.load("ball2.jpg")
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
            pion=pionek(ball, (row,col),ball2)
            player1.append(pion)
            #((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))

    for row in range(5,9):
        for col in range(4):
            pion=pionek(ball1, (row,col),ball2)
            player2.append(pion)
            #surface.blit(ball, ((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict["pos"]
            for pion in player1:
                if pion.contains_point(posn_of_click):
                    pion.handle_click()
                    pion1.handl_unclick()
                    pion1=pion
                break

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

