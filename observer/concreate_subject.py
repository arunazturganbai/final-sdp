from observer.subject import FoodSubject

class FoodReadyConcreteSubject(FoodSubject):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def do_something(self):
        print("Food is prepared!")
        self.notify_observers()
