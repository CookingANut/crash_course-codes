import pygame
import sys

class My_images():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load(r"chapter12\images\java_cup.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def moving(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 2
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 2
    def blit_image(self):
        self.screen.blit(self.image,self.rect)


def check_events(java_cup):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                java_cup.moving_right = True
            if event.key == pygame.K_LEFT:
                java_cup.moving_left = True
            if event.key == pygame.K_UP:
                java_cup.moving_up = True
            if event.key == pygame.K_DOWN:
                java_cup.moving_down = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                java_cup.moving_right = False
            if event.key == pygame.K_LEFT:
                java_cup.moving_left = False
            if event.key == pygame.K_UP:
                java_cup.moving_up = False
            if event.key == pygame.K_DOWN:
                java_cup.moving_down = False

        
pygame.init()
background_color = (217,209,207)
screen = pygame.display.set_mode((1600,1000))
pygame.display.set_caption("Java Cup")
java_cup = My_images(screen)

def run_game():
    while True:
        screen.fill(background_color)
        check_events(java_cup)
        java_cup.moving()
        java_cup.blit_image()
        pygame.display.flip()

run_game()