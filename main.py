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
        self.matrix = [[0]*10 for _ in range(20)]
        self.point = [-1,-1]
    
    def event_per_sec(self):
        self.time+=1
        try:
            self.point[1]+=1
            self.matrix[self.point[1]][5]=1
            self.matrix[self.point[1]-1][5]=0
        except:
            pass

    def draw(self):
        self.window.fill(self.black)
        for row in range(20):
            for column in range(10):
                if (self.matrix[row][column]==0):
                    pygame.draw.rect(self.window,(self.gray),[
                    column*(self.square_height+self.margin),
                    row*(self.square_height+self.margin),
                    self.square_width,
                    self.square_height
                    ])
                elif (self.matrix[row][column]==1):
                    pygame.draw.rect(self.window,(self.red),[
                    column*(self.square_height+self.margin),
                    row*(self.square_height+self.margin),
                    self.square_width,
                    self.square_height
                    ])
                
        time = self.font.render('Time: {}'.format(self.time), False, self.white)
        self.window.blit(time, (0,640))
        pygame.display.update()

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

            self.draw()
            
        pygame.quit()

if __name__ == '__main__':
    tetris=Tetris()
    tetris.main()
