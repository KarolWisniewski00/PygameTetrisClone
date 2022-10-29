import pygame

class Tetris:
    def __init__(self):
        pygame.display.set_caption('Tetris')
        pygame.font.init()
        WIDTH, HEIGHT = 400,800
        self.fps=60
        self.black=(0,0,0)
        self.white=(255,255,255)
        self.gray=(105,105,105)
        self.red=(220,20,60)
        self.square_width, self.square_height = 30,30 
        self.margin=1
        self.time=0
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.matrix_width = 10
        self.matrix_height = 20
        self.matrix = [[0]*self.matrix_width for _ in range(self.matrix_height)]
        self.position = [4,0]

    def move_down_tetrimino(self):
        try:
            if self.matrix[self.position[1]+1][self.position[0]] == 0:
                self.position[1]+=1
            else:
                self.matrix[self.position[1]][self.position[0]] = 1
                self.position = [4,0]
        except:
            self.matrix[self.position[1]][self.position[0]] = 1
            self.position = [4,0]
    
    def event_per_sec(self):
        self.time+=1
        self.move_down_tetrimino()

    def draw_background(self):
        self.window.fill(self.black)
        for row in range(self.matrix_height):
            for column in range(self.matrix_width):
                if self.matrix[row][column]==0:
                    pygame.draw.rect(self.window,(self.gray),[
                    column*(self.square_height+self.margin),
                    row*(self.square_height+self.margin),
                    self.square_width,
                    self.square_height
                    ])
                elif self.matrix[row][column]==1:
                    pygame.draw.rect(self.window,(self.red),[
                    column*(self.square_height+self.margin),
                    row*(self.square_height+self.margin),
                    self.square_width,
                    self.square_height
                    ])

        time = self.font.render('Time: {}'.format(self.time), False, self.white)
        self.window.blit(time, (0,640))

    def draw_tetrimino(self):
        pygame.draw.rect(self.window,(self.red),[
        self.position[0]*(self.square_height+self.margin),
        self.position[1]*(self.square_height+self.margin),
        self.square_width,
        self.square_height
        ])
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
                        if self.position[0]>0:
                            self.position[0] -= 1
                    if event.key == pygame.K_RIGHT:
                        if self.position[0]<self.matrix_width-1:
                            self.position[0] += 1
                    if event.key == pygame.K_DOWN:
                        self.move_down_tetrimino()

            self.draw()
            
        pygame.quit()

if __name__ == '__main__':
    tetris=Tetris()
    tetris.main()
