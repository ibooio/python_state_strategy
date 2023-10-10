from __future__ import annotations
from abc import ABC, abstractmethod

# Partida
class Context:

    def __init__(self, state: State) -> None:
        self.__state = None
        self.transition_to(state)

    @property
    def state(self):
        return self.__state

    def transition_to(self, state: State):        
        self.__state = state
        self.__state.context = self
        print(self.__state.description)

    def confirm(self):
        self.__state.confirm()

    def cancel(self):
        self.__state.cancel()


class State(ABC):

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description) -> None:
        self._description = description

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def confirm(self) -> None:
        pass

    @abstractmethod
    def cancel(self) -> None:
        pass

class Pendiente(State):
    def __init__(self) -> None:
        self._description = "En espera..."

    def confirm(self) -> None:
        self.context.transition_to(BuscandoRival())

    def cancel(self) -> None:
        print("No hacemos nada")


class BuscandoRival(State):
    def __init__(self) -> None:
        self._description = "Buscando rival..."

    def confirm(self) -> None:
        print("Establciendo conexión con el servidor")
        print("Solicitando busqueda de rival")
        print("Esperando respuesta del servidor")
        self.context.transition_to(RivalEncontrado())

    def cancel(self) -> None:
        self.context.transition_to(Pendiente())

class RivalEncontrado(State):
    def __init__(self) -> None:
        self._description = "Rival encontrado..."

    def confirm(self) -> None:
        self.context.transition_to(Comenzando())

    def cancel(self) -> None:
        self.context.transition_to(Pendiente())


class Comenzando(State):
    def __init__(self) -> None:
        self._description = "Comenzando..."

    def confirm(self) -> None:
        print("Yo ignoro este evento")

    def cancel(self) -> None:
        self.context.transition_to(RivalEncontrado())

#if __name__ == "__main__":
    ## The client code.
#
    #context = Context(Pendiente())
    #context.confirm()
    #context.cancel()