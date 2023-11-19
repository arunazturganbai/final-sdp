from abc import ABC, abstractmethod

class FoodButton(ABC):
    @abstractmethod
    def decorate(self):
        pass
