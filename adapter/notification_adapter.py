from adapter.target import Target

class NotificationAdapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def notify(self):
        self.adaptee.notify()
