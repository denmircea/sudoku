import gameWindow
import constants
class squareButton:
    def __init__(self, color, x=0, y=0, text=''):
        self.x = x
        self.y = y
        self.width = constants.SQUARE
        self.height = constants.SQUARE
        self.text = text
        self.color = color
        self.textColor = constants.RED

    def setTextColor(self, color):
        self.textColor = color

    def setxy(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color=constants.WHITE):
        gameWindow.pygame.draw.rect(gameWindow.screen, color, (self.x, self.y, self.width, self.height), 0)

    def setText(self, text, fontSize=30):
        text=str(text)

        if text == '0':
            self.text = ''
        else:
            self.text = str(text)
        font = gameWindow.pygame.font.SysFont(gameWindow.pygame.font.get_default_font(), fontSize)
        text = font.render(str(self.text), True, self.textColor)
        gameWindow.screen.blit(text,
                    (int(self.x + self.width / 2 - text.get_width() / 2),
                     int(self.y + self.height / 2 - text.get_height() / 2)))
    def pressed(self,mousePos):
        if (self.x + self.width >= mousePos[0] and self.y + self.height >= mousePos[1]) and \
                (self.x <= mousePos[0] and self.y <= mousePos[1]):
            return 1
        return 0


class circleButton(squareButton):
    def __init__(self):
        squareButton.__init__(self, constants.WHITE)
        self.radius = constants.SQUARE/2

    def draw(self, color=constants.WHITE):
        gameWindow.pygame.draw.circle(gameWindow.screen, color, (self.x, self.y), int(constants.SQUARE / 2), 0)

    def setText(self, text):
        self.text=text
        if(text==0):
            text="DEL"
        font = gameWindow.pygame.font.SysFont(gameWindow.pygame.font.get_default_font(), 30)
        text = font.render(str(text), True, constants.BLACK)
        gameWindow.screen.blit(text,
                    (int(self.x - text.get_width() / 2),
                     int(self.y - text.get_height() / 2)))
    def pressed(self,mousePos):
        dist = (self.x-mousePos[0])*(self.x-mousePos[0]) + (self.y-mousePos[1])*(self.y-mousePos[1])
        if dist <= self.radius*self.radius:
            return 1
        return 0
