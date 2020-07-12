import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("12_4 python_work")

def run():
    while True:
        screen 
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
        pygame.display.flip()

run()
        