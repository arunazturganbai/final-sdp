from factory.button_factory import ButtonFactory
from factory.menu_button import MenuButton

class MenuButtonFactory(ButtonFactory):
    def create_button(self):
        return MenuButton()

