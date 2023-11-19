from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def display(self):
        pass
