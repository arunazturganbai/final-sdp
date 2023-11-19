from abc import ABC, abstractmethod

class MenuStrategy(ABC):
    @abstractmethod
    def display_menu(self):
        pass
