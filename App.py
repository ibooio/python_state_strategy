import pygame
from Game import *
from Strategy import *

class App():
    def __init__(self) -> None:
        self.__context = Context(Pendiente())
        self.__controller = None
        self.__useController = False
        self.__running = True
        #self.__inputStrategies = [ControllerStrategy(), KeyboardStrategy()]
        self.__controllerStrategy = ControllerStrategy()
        self.__keyboardStrategy = KeyboardStrategy()

    def run(self):
        pygame.init()

        pygame.joystick.init()
        if (pygame.joystick.get_count()):
            self.__initController()
        self.__initGui()

        while self.__running:
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.__running = False
                
                if event.type == pygame.JOYBUTTONDOWN:
                    self.__controllerStrategy.processEvent(pygame, event, self.__context)
                
                if event.type == pygame.KEYDOWN:
                    self.__keyboardStrategy.processEvent(pygame, event, self.__context)
                
            self.__drawGui()
        pygame.quit()

    def __initGui(self):
        self.__screen = pygame.display.set_mode((1280, 720))

    def __drawGui(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        pressX = font.render('Presione X para continuar', True, (0, 0, 0))
        pressB = font.render('Presione B para cancelar', True, (0, 0, 0))
        self.__screen.fill("white")
        self.__screen.blit(pressX, (100,100))
        self.__screen.blit(pressB, (100,200))
        statusText = font.render('Estado: ' + self.__context.state.description, True, (0, 0, 0))
        self.__screen.blit(statusText, (100,300))
        pygame.display.flip()



    def __initController(self):
        self.__useController = True
        self.__controller = pygame.joystick.Joystick(0)
        self.__controller.init()     
    
    def __removeController(self):
        self.__controller = None
        self.__useController = False        


app = App()
app.run()