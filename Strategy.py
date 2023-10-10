from __future__ import annotations
from abc import ABC, abstractmethod

class InputStrategy(ABC):
    @abstractmethod
    def processEvent(self, pygame, event, context) -> None:
        pass

class ControllerStrategy(InputStrategy):          
    def processEvent(self, pygame, event, context):
        #if event.type == pygame.JOYBUTTONDOWN:
        if (event.button == 0):
            context.confirm()
        if (event.button == 1):
            context.cancel()
        print("Procesado por ControllerStrategy")
            

class KeyboardStrategy(InputStrategy):
    def processEvent(self, pygame, event, context):
        #if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_n:
            context.confirm()
        if event.key == pygame.K_a:
            context.confirm()
        if event.key == pygame.K_b:
            context.cancel()
        print("Procesado por KeyboardStrategy")