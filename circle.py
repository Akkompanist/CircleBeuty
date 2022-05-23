import pygame
import math
import menu

class Circle:
    def __init__(self, screen_size, var, color_type):
            self.screen_size = screen_size
            self.size = (self.screen_size[0]//3, self.screen_size[1]//3)

            self.circles_cord = []
            self.circles_cord2 = []

            self.pi = 3.14
            self.variable = float(0)
            self.text_size = 50
            self.var = var
            self.plus_var = 2**var
            self.first_run = True

            self.num_of_dots = 180
            self.divide = self.num_of_dots/360 
            self.save_nod = self.num_of_dots
            self.num_of_dots *= 2
            
            self.color_type = color_type
            self.color = 0 if self.color_type == 2 or self.color_type == 1 else 255
            self.color_variable = 1

            for i in range (self.num_of_dots):
                if i < self.save_nod:
                    self.circles_cord.append(((self.size[0] * math.cos((i/self.divide)*self.pi/180))+self.size[0]*1.5, (self.size[1] * math.sin((i/self.divide)*self.pi/180)+self.size[1]*1.5)))
                if i > self.save_nod:
                    self.circles_cord2.append(((int(self.size[0]/2) * math.cos((i/self.divide)*self.pi/180))+self.size[0]*1.5, (int(self.size[1]/2) * math.sin((i/self.divide)*self.pi/180)+self.size[1]*1.5)))

            pygame.init()
            self.screen = pygame.display.set_mode(self.screen_size)
            self.clock = pygame.time.Clock()

    def inver_color(self, color):
            r1 = 255-color[0]
            r2 = 255-color[1]
            r3 = 255-color[2]
            return (r1,r2,r3)

    def add_color(self, color):
            color += self.color_variable
            if color >= 255:
                self.color_variable *= -1
                color += self.color_variable
            if color < 0:
                self.color_variable *= -1
                color += self.color_variable
            return color

    def stop(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN: 
                            return
    def run(self):
            while 1:
                if (self.color_type == 2): self.color = self.add_color(self.color)
                self.color_for_circle = (self.color,self.color,self.color)
                self.color_for_bg = self.inver_color(self.color_for_circle)
                self.screen.fill(self.color_for_bg)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        menu.Menu()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN: 
                                self.stop()

                            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                               self.plus_var *= -1 
                               self.variable += self.plus_var
                            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                               self.plus_var *= 2 
                               self.variable += self.plus_var
                    if event.type == pygame.KEYUP:
                            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                self.plus_var *= -1 
                                self.variable += self.plus_var
                            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                               self.plus_var /= 2 
                               self.variable += self.plus_var

                # pygame.draw.line(self.screen, "gray", (self.screen_size[0]/2, 0), (self.screen_size[0]/2, self.screen_size[1]), 1)
                # pygame.draw.line(self.screen, "gray", (0, self.screen_size[1]/2), (self.screen_size[1], self.screen_size[1]/2), 1 )

                font = pygame.font.Font(None, self.text_size)
                text = font.render(str(self.variable), True, self.color_for_circle)
                text_rect = text.get_rect(center=(self.screen_size[0]//2, self.text_size))

                self.screen.blit(text , text_rect)

                for i in self.circles_cord:
                    pygame.draw.circle(self.screen, self.color_for_circle, (i[0], i[1]), 1)

                if self.variable >= 0:
                    for i in range(len(self.circles_cord)-1):
                        save_num = i*self.variable 
                        while save_num > len(self.circles_cord)-1:
                            save_num -= len(self.circles_cord)+1
                        save_num = int(save_num)
                        pygame.draw.line(self.screen, self.color_for_circle, (self.circles_cord[i][0], self.circles_cord[i][1]), (self.circles_cord[save_num][0], self.circles_cord[save_num][1]), 1 )
                   
                    for i in range(len(self.circles_cord2)-1):
                        save_num = i*self.variable*2
                        while save_num > len(self.circles_cord2)-1:
                            save_num -= len(self.circles_cord2)+1
                        save_num = int(save_num)
                        pygame.draw.line(self.screen, self.color_for_circle, (self.circles_cord2[i][0], self.circles_cord2[i][1]), (self.circles_cord2[save_num][0], self.circles_cord2[save_num][1]), 1 )
                
                if self.variable > 0 or self.first_run: 
                    self.variable += self.plus_var
                
                self.first_run = False

                self.clock.tick(60)
                pygame.display.update()
