import constants
def drawTable(mat,inputSudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if inputSudoku[i][j] != '0':
                mat[i][j].setTextColor(constants.BLACK)
            mat[i][j].setxy(15 + j * (constants.SQUARE + 5) + int(j / 3) * 10,
                            15 + i * (constants.SQUARE + 5) + int(i / 3) * 10)
            mat[i][j].draw()
            mat[i][j].setText(inputSudoku[i][j])
def drawCircles(circles):
    for i in range(1,10):
        circles[i].setxy(850, 20 + (i-1) * (constants.SQUARE + 6) + int(constants.SQUARE/2))
        circles[i].draw()
        circles[i].setText(i)
    circles[0].setxy(700, circles[9].y)
    circles[0].setText('0')

    circles[0].draw()
def getInputSudoku():
    file = open("test.in", "r")
    fileinp = file.readlines()
    inputSudoku = []
    for line in fileinp:
        inputSudoku.append(line.strip().split(" "))
    for i in inputSudoku:
        for j in i:
         j=int(j)
    return inputSudoku
def colorSelect(mat,circles, number):
    colorDeselect(mat,circles)
    circles[int(number)].draw(constants.GRAY)
    circles[int(number)].setText(int(number))
    for i in range(0, 9):
        for j in range(0, 9):
            if mat[i][j].text == str(number) :
                mat[i][j].draw(constants.GRAY)
                mat[i][j].setText(mat[i][j].text)



def colorDeselect(mat,circles):
    for i in range(0, 9):
        for j in range(0, 9):
            mat[i][j].draw()
            mat[i][j].setText(mat[i][j].text)
    for i in range(0,10):
        circles[i].draw()
        circles[i].setText(i)
def puzzleCompleted(mat):
    for i in range(0, 9):
        for j in range(0, 9):
            if mat[i][j].text=='':
                return 0
    return 1