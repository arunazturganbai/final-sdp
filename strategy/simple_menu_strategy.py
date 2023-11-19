from strategy.menu_strategy import MenuStrategy
class SimpleMenuStrategy(MenuStrategy):
    def display_menu(self):
        print("Welcome to the Restaurant!")
        print("Menu:")
        print("1. Spaghetti Bolognese - $12.99")
        print("2. Margherita Pizza - $10.99")
        print("3. Caesar Salad - $8.99")
        print("4. Tiramisu - $6.99")
        print("5. Espresso - $3.99")

