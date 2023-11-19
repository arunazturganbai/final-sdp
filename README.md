## Name of your final project: Restaurant Application
#### Group: SE-2215
#### Team members: Tokenova Zhanerke, Salim Aizere, Turganbay Arunaz

## Project Overview:
This project is a simple restaurant application implemented in Python using the tkinter library. The application employs various design patterns, such as the strategy pattern for menu handling, singleton pattern for waiter service, decorator pattern for button decorations, adapter pattern for notifications, observer pattern for food readiness notifications, and factory pattern for button creation.

### Idea of the Project:
The restaurant application is designed to simulate a basic ordering system. It provides a graphical user interface (GUI) where users can view the menu, order food, and call the waiter.

### Purpose of the Work:
The purpose of this project is to demonstrate the implementation of various design patterns in a real-world scenario, showcasing their use and benefits in a restaurant application.

### Objectives of the Work:
1. Implement a strategy pattern for displaying the menu dynamically.
2. Utilize the singleton pattern for the waiter service to ensure a single instance.
3. Apply the decorator pattern to enhance button functionalities.
4. Implement the adapter pattern to adapt food notifications.
5. Use the observer pattern to notify customers when the food is ready.
6. Apply the factory pattern for creating different types of buttons.

## Main Body:

### Design Patterns Used:

#### 1. Strategy Pattern:
   - **Files:** `menu_context.py`, `menu_strategy.py`, `simple_menu_strategy.py`
   - **Explanation:** The strategy pattern is implemented for displaying the restaurant menu dynamically.

#### 2. Singleton Pattern:
   - **File:** `waiter_service.py`
   - **Explanation:** The singleton pattern ensures that there is only one instance of the waiter service.

#### 3. Decorator Pattern:
   - **Files:** `order_button_decorator.py`, `call_waiter_button_decorator.py`
   - **Explanation:** Decorator pattern is used to enhance the functionalities of order and call waiter buttons.

#### 4. Adapter Pattern:
   - **Files:** `notification_adapter.py`, `food_notification.py`
   - **Explanation:** The adapter pattern is employed to adapt the `FoodNotification` class to the `Target` interface.

#### 5. Observer Pattern:
   - **Files:** `food_ready_subject.py`, `customer_observer.py`, `observer.py`, `subject.py`
   - **Explanation:** Observer pattern is used for notifying customers when the food is ready.

#### 6. Factory Pattern:
   - **Files:** `menu_button_factory.py`, `order_button_factory.py`, `button_factory.py`, `menu_button.py`, `order_button.py`, `button.py`
   - **Explanation:** Factory pattern is implemented for creating different types of buttons.

### GUI Elements:
- **Display Menu Button:** Displays the restaurant menu using the strategy pattern.
- **Call Waiter Button:** Calls the waiter using the singleton pattern.
- **Order Food Button:** Places a food order, demonstrating decorator, adapter, and observer patterns.

## UML Diagram:
![UML Diagram](https://github.com/arunazturganbai/final-sdp/blob/main/uml%20diagram.png)

## Conclusion:

### Key Points:
- The project successfully implements various design patterns to create a functional restaurant application.
- Design patterns enhance code modularity, reusability, and maintainability.

### Project Outcomes:
- Achieved a modular and flexible code structure.
- Successfully demonstrated the implementation of multiple design patterns.

### Challenges Faced:
- Ensuring proper integration of different design patterns.
- Simulating the ordering process and food preparation logic.

### Future Improvements:
- Expand the menu and ordering logic for a more realistic simulation.
- Implement a database to store and retrieve menu items.
- Enhance the GUI for a more user-friendly experience.
