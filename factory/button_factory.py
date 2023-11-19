from abc import ABC, abstractmethod
from factory.button import Button

class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
