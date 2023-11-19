from observer.observer import Observer

class CustomerObserver(Observer):
    def update(self):
        print("Food is ready! Enjoy your meal!")
