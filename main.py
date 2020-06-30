import pygame
import constants
import table
import buttons
import gameWindow


def click(mousePos):
    for i in range(0, 9):
        for j in range(0, 9):
            if mat[i][j].pressed(mousePos):
                if mat[i][j].text == '' and 1 <= (int)(constants.selectedValue) <= 9:
                    mat[i][j].draw(constants.GRAY)
                    mat[i][j].setText(int(constants.selectedValue))
                elif constants.selectedValue == 0 and int(inputSudoku[i][j]) == 0:
                    mat[i][j].draw()
                    print(inputSudoku[i][j])
                    mat[i][j].setText(int(constants.selectedValue))
                elif mat[i][j].text != str(constants.selectedValue) and constants.selectedValue !=0:
                    constants.selectedValue = int(mat[i][j].text)
                    table.colorSelect(mat, circles, constants.selectedValue)
    for i in range(0, 10):
        if circles[i].pressed(mousePos):
            constants.selectedValue = int(circles[i].text)
            table.colorSelect(mat, circles, constants.selectedValue)


# setup game
pygame.init()
start = buttons.squareButton(constants.BLACK)
running = bool(gameWindow.welcomeScreen(start))
mat = [[buttons.squareButton(constants.WHITE) for x in range(9)] for y in range(9)]
circles = [buttons.circleButton() for x in range(10)]
inputSudoku = table.getInputSudoku()
table.drawTable(mat, inputSudoku)
table.drawCircles(circles)
table.colorSelect(mat, circles, constants.selectedValue)
while running:
    pygame.display.update()
    if table.puzzleCompleted(mat) :
        running = gameWindow.win(start)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click(event.pos)

