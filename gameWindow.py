import constants
import pygame
import time

# create screen

screen = pygame.display.set_mode((constants.widthScreen, constants.heigthScreen))
pygame.display.set_caption("Sudoku by Mircea")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


def welcomeScreen(start):
    pygame.init()
    screen.fill(constants.WHITE)
    screen.blit(icon, (0, 20))
    start.setxy(600, 400)
    start.width = 300
    start.height = 60
    start.setTextColor(constants.WHITE)
    start.draw(constants.BLACK)
    start.setText("Start game", 70)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start.pressed(event.pos):
                        screen.fill(constants.BLACK)
                        screen.blit(screen, (0, 0))
                        pygame.display.update()
                        return 1


def win(start):
    screen.fill(constants.WHITE)
    screen.blit(icon, (0, 20))
    start.setxy(600, 400)
    start.width = 300
    start.height = 60
    start.setTextColor(constants.WHITE)
    start.draw(constants.BLACK)
    start.setText("YOU WIN", 70)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
    return 0
