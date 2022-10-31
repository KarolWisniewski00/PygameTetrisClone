import pygame
import random

class Tetris:
    def __init__(self):
        pygame.display.set_caption('Tetris')
        pygame.font.init()
        WIDTH, HEIGHT = 400,800
        self.fps=60
        self.black=(0,0,0)
        self.white=(255,255,255)
        self.gray=(105,105,105)
        self.red = (220,20,60)
        self.gray_2 = (192,192,192)
        self.blue = (0,191,255)
        self.yellow = (204,204,0)
        self.pink = (255,105,180)
        self.blue_2 = (0,0,255)
        self.green = (50,205,50)
        self.square_width, self.square_height = 30,30 
        self.margin=1
        self.time=0
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.matrix_width = 10
        self.matrix_height = 20
        self.matrix = [[0]*self.matrix_width for _ in range(self.matrix_height)]
        self.position = [4,0]
        self.tetriminos = ['I','T','O','L','J','S','Z']
        self.save_shape(random.choice(self.tetriminos))

    def save_shape(self, now):
        if now == 'I':
            self.shape = [[1],[1],[1],[1]]
            self.color = self.red
            self.color_number = 1
        elif now == 'T':
            self.shape = [[2,2,2],[0,2,0]]
            self.color = self.gray_2
            self.color_number = 2
        elif now == 'O':
            self.shape = [[3,3],[3,3]]
            self.color = self.blue
            self.color_number = 3
        elif now == 'L':
            self.shape = [[4,0],[4,0],[4,4]]
            self.color = self.yellow
            self.color_number = 4
        elif now == 'J':
            self.shape = [[0,5],[0,5],[5,5]]
            self.color = self.pink
            self.color_number = 5
        elif now == 'S':
            self.shape = [[0,6,6],[6,6,0]]
            self.color = self.blue_2
            self.color_number = 6
        elif now == 'Z':
            self.shape = [[7,7,0],[0,7,7]]
            self.color = self.green
            self.color_number = 7

    def save_shape_in_matrix(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column]!=0:
                    self.matrix[self.position[1]+row][self.position[0]+column] = self.color_number
        self.save_shape(random.choice(self.tetriminos))
        self.position = [4,0]

    def check(self,value_row, value_column):
        all_ok = True
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column]!=0:
                    if self.matrix[self.position[1]+row+value_row][self.position[0]+column+value_column] != 0:
                        all_ok = False
        return all_ok

    def move_tetrimino(self, direction):
        if direction == 'down':
            try:
                all_ok = self.check(1,0)
                if all_ok == True:
                    self.position[1]+=1
                else:
                    self.save_shape_in_matrix()
            except:
                self.save_shape_in_matrix()

        elif direction == 'left':
            if self.position[0]>0:
                try:
                    all_ok = all_ok = self.check(0,-1)
                    if all_ok == True:
                        self.position[0]-=1
                except:
                    pass
        
        elif direction == 'right':
            if self.position[0]<self.matrix_width-1:
                try:
                    all_ok = self.check(0,1)
                    if all_ok == True:
                        self.position[0]+=1
                except:
                    pass
    
    def event_per_sec(self):
        self.time+=1
        self.move_tetrimino('down')

    def draw_square(self, color, column, row):
        pygame.draw.rect(self.window,(color),[
        column*(self.square_height+self.margin),
        row*(self.square_height+self.margin),
        self.square_width,
        self.square_height
        ])

    def draw_background(self):
        self.window.fill(self.black)
        for row in range(self.matrix_height):
            for column in range(self.matrix_width):
                if self.matrix[row][column]==0:
                    self.draw_square(self.gray,column,row)
                elif self.matrix[row][column]==1:
                    self.draw_square(self.red,column,row)
                elif self.matrix[row][column]==2:
                    self.draw_square(self.gray_2,column,row)
                elif self.matrix[row][column]==3:
                    self.draw_square(self.blue,column,row)
                elif self.matrix[row][column]==4:
                    self.draw_square(self.yellow,column,row)
                elif self.matrix[row][column]==5:
                    self.draw_square(self.pink,column,row)
                elif self.matrix[row][column]==6:
                    self.draw_square(self.blue_2,column,row)
                elif self.matrix[row][column]==7:
                    self.draw_square(self.green,column,row)

        time = self.font.render('Time: {}'.format(self.time), False, self.white)
        self.window.blit(time, (0,640))

    def draw_tetrimino(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[row])):
                if self.shape[row][column]!=0:
                    self.draw_square(self.color,self.position[0]+column,self.position[1]+row)

        pygame.display.update()

    def draw(self):
        self.draw_background()
        self.draw_tetrimino()

    def main(self):
        run = True
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        while run:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.USEREVENT:
                    self.event_per_sec()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_tetrimino('left')
                    if event.key == pygame.K_RIGHT:
                        self.move_tetrimino('right')
                    if event.key == pygame.K_DOWN:
                        self.move_tetrimino('down')

            self.draw()
            
        pygame.quit()

if __name__ == '__main__':
    tetris=Tetris()
    tetris.main()
