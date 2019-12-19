import sys
import pygame
from pygame.locals import *
from pygame import *
from playsound import playsound

# font = pygame.font.SysFont('Arial', 25)


class Game(object):
    amount = ["1,00,00,000", "50,00,000", "25,00,000", "12,50,000", "6,25,000",
              "3,20,000", "1,60,000", "80,000", "40,000", "20,000", "10,000"]
    questionList = [
        {
            "question": "Which of the following is not a framework?",
            "options": ["A)ExpressJs", "B)Django", "C)PHP", "D)Laravel"],
            "answer": 2
        },
        {
            "question": "Which graphics rendering engine is used in Flutter?",
            "options": ["A)Nvidia", "B)Gecko", "C)Blink", "D)Skia"],
            "answer": 3
        },
        {
            "question": "Which HTTP status codes correspond to Server error?",
            "options": ["A)4XX", "B)5XX", "C)3XX", "D)2XX"],
            "answer": 1
        },
        {
            "question": "Which is the best searching algorithm in terms of time complexity?",
            "options": ["A)Linear Search", "B)Binary Search", "C)Ternary Search", "D)BFS"],
            "answer": 1
        },
        {
            "question": "Which command shows the record of all commits?",
            "options": ["A)git commit -a", "B)git log", "C)git reflog", "D)git status"],
            "answer": 2
        },
        {
            "question": "What is the fundamental unit of Quantum Computing?",
            "options": ["A)Qubit", "B)Cubit", "C)Byte", "D)Bit"],
            "answer": 0
        },
        {
            "question": "Who created Java?",
            "options": ["A)Guido van Rossum", "B)Dennis Ritchie", "C)Bjarne Stroustrup", "D)James Gosling"],
            "answer": 3
        },

        {
            "question": "What does typeof typeof 1 will return?",
            "options": ["A)number", "B)string", "C)object", "D)function"],
            "answer": 1
        },
        {
            "question": "Which DB engine use Key-Value store?",
            "options": ["A)MongoDB", "B)MySql", "C)Redis", "D)PostgreSQL"],
            "answer": 2
        },
        {
            "question": "Number of nodes in Perfect Binary Tree of height h?",
            "options": ["A)2^h", "B)2^(h-1)", "C)2^h-1", "D)2*h"],
            "answer": 2
        },
        {
            "question": "Which is a self balancing tree with height difference atmost 1?",
            "options": ["A)AVL Tree", "B)Red Black Tree", "C)Segment Tree", "D)Skew Tree"],
            "answer": 0
        },
    ]
    ans_key = [1, 3, 1, 0, 1, 1, 2, 1, 3, 3, 0, 0, 2, 2]
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    currentQuestion = 0
    selectedAnswer = -1
    red = (200, 20, 20)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    orange = (255, 128, 0)
    navyBlue = (156, 101, 226)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('KBC Pygame')
        self.screen = pygame.display.set_mode((1366, 768), 0, 32)
        self.addBackgroudPic()
        self.font = pygame.font.SysFont('Arial', 25)
        self.bigFont = pygame.font.SysFont('Arial', 50)

    def addBackgroudPic(self):
        bg = pygame.image.load("kbc.jpg")
        bg = pygame.transform.scale(bg, (1366, 768))
        self.screen.blit(bg, (0, 0)) #To draw surface on screen at given position (x,y) 

    def RoundedRectangle(self, rect, color, radius=0.4):
        """
        RoundedRectangle(surface,rect,color,radius=0.4)

        surface : destination
        rect    : rectangle
        color   : rgb or rgba
        radius  : 0 <= radius <= 1
        """
        # color = (156, 101, 226)
        rect = Rect(rect)
        color = Color(*color)
        alpha = color.a
        color.a = 0
        pos = rect.topleft
        rect.topleft = 0, 0
        rectangle = Surface(rect.size, SRCALPHA)
        circle = Surface([min(rect.size)*3]*2, SRCALPHA)
        draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle = transform.smoothscale(circle, [int(min(rect.size)*radius)]*2)
        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)
        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)
        return self.screen.blit(rectangle, pos)

    def addPriceTile(self):
        yCordinate = 50
        yCordinateText = 75
        for index in range(11):
            if 10-index == self.currentQuestion:
                self.RoundedRectangle(
                    (50, yCordinate, 200, 50), self.red, 0.5)
            else:
                self.RoundedRectangle(
                    (50, yCordinate, 200, 50), self.navyBlue, 0.5)
            self.displayText(self.amount[index],
                             self.WHITE, 150, yCordinateText)
            yCordinate += 60
            yCordinateText += 60

    def addQuestionBox(self):
        self.RoundedRectangle(
            (320, 450, 950, 100), self.navyBlue, 0.5)
        self.displayText(
            self.questionList[self.currentQuestion]["question"], self.WHITE, 825, 500)

    def addOptionBox(self, isCorrect=False):
        yCordinate = 560
        yCordinateText = 580
        xCordinate = 320
        xCordinateText = 450
        options = self.questionList[self.currentQuestion]["options"]
        for index in range(len(options)):
            if self.selectedAnswer == index:
                if isCorrect:
                    self.RoundedRectangle(
                        (xCordinate, yCordinate, 300, 50), self.green, 0.5)
                else:
                    self.RoundedRectangle(
                        (xCordinate, yCordinate, 300, 50), self.red, 0.5)
            else:
                self.RoundedRectangle(
                    (xCordinate, yCordinate, 300, 50), self.navyBlue, 0.5)
            self.displayText(
                options[index], self.WHITE, xCordinateText, yCordinateText)
            if(index % 2 == 0):
                xCordinate = 950
                xCordinateText = 1070
            else:
                xCordinate = 320
                yCordinate = 620
                xCordinateText = 450
                yCordinateText = 640

    def validateAnswer(self, correctAnswer, keyPressed):
        print("correctAnswer==>{0}".format(correctAnswer))
        isValid = False
        if keyPressed == pygame.K_a:
            self.selectedAnswer = 0
            if correctAnswer == 0:
                isValid = True
            else:
                isValid = False
        if keyPressed == pygame.K_b:
            self.selectedAnswer = 1
            if correctAnswer == 1:
                isValid = True
            else:
                isValid = False
        if keyPressed == pygame.K_c:
            self.selectedAnswer = 2
            if correctAnswer == 2:
                isValid = True
            else:
                isValid = False
        if keyPressed == pygame.K_d:
            self.selectedAnswer = 3
            if correctAnswer == 3:
                isValid = True
            else:
                isValid = False
        return isValid

    def gameRules(self):
        self.addBackgroudPic()
        readRules = True
        isPlay=True
        while readRules:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        readRules = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.displayText("Welcome to KBC Game For Developers",
                             self.red,
                             630, 50, True
                             )
            self.displayText("Game Rules:-",
                             self.green,
                             680, 100, True)
            self.displayText("Press A/B/C/D to select corresponding options",
                             self.orange,
                             680, 150, True)
            self.displayText("Press P to play or Q to quit.",
                             self.WHITE,
                             660, 650, True)
            # if isPlay:
            #     playsound("KBCIntro.mp3")
            #     isPlay = False
            pygame.display.update()

    def displayText(self, text, color, xCordinate, yCordinate=0, isBig=False):
        if isBig:
            textSurface = self.bigFont.render(text, True, color)
        else:
            textSurface = self.font.render(text, True, color)
        textRectangle = textSurface.get_rect()
        textRectangle.center = (xCordinate, yCordinate)
        self.screen.blit(textSurface, textRectangle)

    def resultScreen(self, isLost=False):
        isPlay = True
        self.addBackgroudPic()
        readRules = True
        while readRules:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        readRules = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            # self.screen.fill(self.WHITE)
            wonAmount = 0
            if self.currentQuestion > 0:
                wonAmount = self.amount[10-(self.currentQuestion-1)]
            if isLost:
                self.displayText("Oops You have lost the game!!! ",
                                 self.red,
                                 630, 50, True
                                 )
                self.displayText("Better luck next time",
                                 self.green,
                                 680, 100, True)
            else:
                self.displayText("Well Played!!!",
                                 self.red,
                                 630, 50, True
                                 )
                self.displayText("You have won:-"+str(wonAmount) + " INR",
                                 self.green,
                                 680, 100, True)
            self.displayText("Press P to play again or Q to end the game.",
                             self.WHITE,
                             660, 650, True)
            pygame.display.update()
            if isPlay:
                playsound("KbcIntro.mp3")
                isPlay = False
        self.currentQuestion = 0
        self.selectedAnswer = -1
        self.playGame()

    def playGame(self):
        playsound("KBCIntro.mp3")
        self.addBackgroudPic()
        self.addPriceTile()
        self.addQuestionBox()
        self.addOptionBox()
        correctAnswer = self.questionList[self.currentQuestion]["answer"]
        play = True
        proceed = True
        isPlay = True
        while play:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        # self.currentQuestion += 1
                        self.resultScreen()
                    elif (event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]):
                        isCorrect = self.validateAnswer(
                            correctAnswer, event.key)
                        self.addOptionBox(isCorrect=isCorrect)
                        pygame.display.update()
                        pygame.time.delay(2000)
                        if isCorrect:
                            self.currentQuestion += 1
                            self.selectedAnswer = -1
                            if self.currentQuestion > 10:
                                # Winner Screen
                                self.resultScreen()
                            else:
                                correctAnswer = self.questionList[self.currentQuestion]["answer"]
                                self.addPriceTile()
                                self.addQuestionBox()
                                self.addOptionBox()
                                pygame.display.update()
                                playsound("KbcQuestion.mp3")
                        else:
                            play = False
                            pass
                            # GameOver
                            self.resultScreen(isLost=True)
            pygame.display.update()
            if isPlay:
                playsound("KbcQuestion.mp3")
                isPlay = False


if __name__ == '__main__':
    game = Game()
    game.gameRules()
    game.playGame()
