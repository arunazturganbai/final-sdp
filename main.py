import tkinter as tk
from tkinter import messagebox
from strategy.menu_context import MenuContext
from strategy.simple_menu_strategy import SimpleMenuStrategy
from singleton.waiter_service import WaiterService
from decorator.order_button_decorator import OrderButtonDecorator
from decorator.call_waiter_button_decorator import CallWaiterButtonDecorator
from adapter.notification_adapter import NotificationAdapter
from adapter.food_notification import FoodNotification
from observer.food_ready_subject import FoodReadySubject
from observer.customer_observer import CustomerObserver
from factory.menu_button_factory import MenuButtonFactory
from factory.order_button_factory import OrderButtonFactory

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Application")

        # Create strategy components
        menu_strategy = SimpleMenuStrategy()
        self.menu_context = MenuContext(menu_strategy)

        # Create singleton component
        self.waiter = WaiterService()

        # Create decorator components
        self.order_button = OrderButtonDecorator()
        self.call_waiter_button = CallWaiterButtonDecorator()

        # Create adapter components
        self.food_notification = FoodNotification()
        self.notification_adapter = NotificationAdapter(self.food_notification)

        # Create observer components
        self.food_subject = FoodReadySubject()
        self.customer_observer = CustomerObserver()
        self.food_subject.add_observer(self.customer_observer)

        # Create factory components
        self.menu_button_factory = MenuButtonFactory()
        self.order_button_factory = OrderButtonFactory()

        # Set up GUI elements
        self.menu_button = tk.Button(root, text="Display Menu", command=self.display_menu)
        self.call_waiter_btn = tk.Button(root, text="Call Waiter", command=self.call_waiter)
        self.order_food_btn = tk.Button(root, text="Order Food", command=self.order_food)

        # Arrange GUI elements
        self.menu_button.pack(pady=10)
        self.call_waiter_btn.pack(pady=10)
        self.order_food_btn.pack(pady=10)

    def display_menu(self):
        message = self.menu_context.display_menu()
        self.show_message(message)

    def call_waiter(self):
        self.waiter.call_waiter()
        self.show_message("Waiter has been called.")

    def order_food(self):
        food_order = self.menu_context.display_menu()  # Replace with actual order logic
        self.order_button.decorate()
        self.call_waiter_button.decorate()
        self.food_notification.notify()

        # Simulate food preparation
        self.food_subject.do_something()
        self.show_message("Food has been ordered and is being prepared.")

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
