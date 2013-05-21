#!/usr/bin/python
import pygame

n = 8         # This is an NxN chess board.
surface_sz = 480           # Proposed physical surface size.
sq_sz = surface_sz // n    # sq_sz is length of a square.
surface_sz = n * sq_sz
ball = pygame.image.load("pion.png")
ball_offset = (sq_sz-ball.get_width()) // 2
tablica =  [[0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]]
surface = pygame.display.set_mode((surface_sz, surface_sz))

class pionek(object):
    def __init__(self,img, posn,img2):
        #pos to (col,row)
        self.image=img
        self.posn = posn
        self.img2=img2
        self.img = img
        self.moves=[]


    def ruch(self, kierunek):
        posn=self.posn
        if kierunek:
            col = posn[1]+1 
        else:
            col = posn[1]-1
        row=posn[2]+1
        tablica[posn[1]][posn[0]]=0
        self.posn=(col,row)
        tablica[row][col]=1
        
    
    def draw(self, surface):
        #surface.blit(self.image, self.posn)
       # print self.posn
        surface.blit(self.image,(self.posn[0]*sq_sz+ball_offset, self.posn[1]*sq_sz+ball_offset))
    
    def contains_point(self, pt):
      """ Return True if my sprite rectangle contains point pt """
      (my_x, my_y) = (self.posn[0]*sq_sz+ball_offset,self.posn[1]*sq_sz+ball_offset)
      my_width = self.image.get_width()
      my_height = self.image.get_height()
      (x, y) = pt
      
      print my_x, my_y
      return ( x >= my_x and x < my_x + my_width and
               y >= my_y and y < my_y + my_height)
    
    def handle_click(self):
        self.img=self.image
        self.image = self.img2
        if tablica[self.posn[1]+1][self.posn[0]+1]==0:
            self.moves.append(((self.posn[0]+1)*sq_sz, (self.posn[1]+1)*sq_sz, sq_sz, sq_sz))
            surface.fill((200,200,200), self.moves[-1])
        elif tablica[self.posn[1]+1][self.posn[0]+1]==2 and tablica[self.posn[1]+2][self.posn[0]+2]==0: 
            self.moves.append(((self.posn[0]+2)*sq_sz, (self.posn[1]+2)*sq_sz, sq_sz, sq_sz))
            surface.fill((200,200,200), self.moves[-1])
        if tablica[self.posn[1]+1][self.posn[0]-1]==0:
            self.moves.append(((self.posn[0]-1)*sq_sz, (self.posn[1]+1)*sq_sz, sq_sz, sq_sz))
            surface.fill((200,200,200), self.moves[-1])
        elif tablica[self.posn[1]+1][self.posn[0]-1]==2 and tablica[self.posn[1]+2][self.posn[0]-2]==0: 
            self.moves.append(((self.posn[0]-2)*sq_sz, (self.posn[1]+2)*sq_sz, sq_sz, sq_sz))
            surface.fill((200,200,200), self.moves[-1])



    def handle_unclick(self):
        self.img2 = self.image
        self.image=self.img
        for i in self.moves:
            surface.fill((255,255,255), i)
        self.moves=[]
def main():
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
    
    ball = pygame.image.load("pion.png")
    ball1 = pygame.image.load("pion1.png")
    ball2 = pygame.image.load("pion2.png")
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
            pion=pionek(ball, (col*2+row%2,row),ball2)
            player1.append(pion)
            print row, col*2+row%2
            tablica[row][col*2+row%2]=1
            #((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))

    for row in range(5,8):
        for col in range(4):
            pion=pionek(ball1, (col*2+row%2,row),ball2)
            player2.append(pion)
            print row, col*2+row%2
            tablica[row][col*2+row%2]=2
            #surface.blit(ball, ((2*col+row%2)*sq_sz+ball_offset,row*sq_sz+ball_offset))
    pion1=pionek(ball, (0,0),ball2)
    print tablica
    click=0

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict["pos"]
            for pion in player1:
                print "\n\n\n", posn_of_click
                if pion.contains_point(posn_of_click):
                    pion1.handle_unclick()
                    pion.handle_click()
                    pion1=pion
                    pygame.display.flip()
                    click=1
                    break
        if ev.type == pygame.MOUSEBUTTONDOWN and click==1: 
            posn_of_click = ev.dict["pos"]
            if posn_of_click[0]/sq_sz== pion1.posn[0]+1:
                pion1.ruch(1)
            elif posn_of_click[0]/sq_sz== pion1.posn[0]-1:
                pion1.ruch(0)

        # Draw a fresh background (a blank chess board)
       
        # Now that squares are drawn, draw the queens.
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == ord("r"):
                for i in player1:
                    print i.posn
        for pion in player1+player2:
            pion.draw(surface)
        pygame.display.flip()


    pygame.quit()

#if __name__ == "__main__":
    #draw_board([0, 5, 3, 1, 6, 4, 2,0])    # 7 x 7 to test window size
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
main()
