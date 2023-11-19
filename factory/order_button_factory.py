from factory.button_factory import ButtonFactory
from factory.order_button import OrderButton

class OrderButtonFactory(ButtonFactory):
    def create_button(self):
        return OrderButton()

