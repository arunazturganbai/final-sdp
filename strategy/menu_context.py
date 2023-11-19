from strategy.menu_strategy import MenuStrategy

class MenuContext:
    def __init__(self, strategy: MenuStrategy):
        self.strategy = strategy

    def display_menu(self):
        self.strategy.display_menu()
