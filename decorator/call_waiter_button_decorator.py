from decorator.food_button import FoodButton

class CallWaiterButtonDecorator(FoodButton):
    def decorate(self):
        print("Call waiter button")
