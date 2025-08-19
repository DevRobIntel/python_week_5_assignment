# Activity 2: Polymorphism Challenge

## Description

This activity demonstrates **Polymorphism** in Object-Oriented Programming (OOP) using Python.
Polymorphism allows different classes to define methods with the same name but provide different implementations.

We implement a set of `Vehicle` classes where each class defines its own version of the `move()` method.

## Features Implemented

### Base Concept

- All classes represent vehicles with a common behavior: `move()`.

### Classes

- **Car**: Implements `move()` to show driving.
- **Plane**: Implements `move()` to show flying.
- **Boat**: Implements `move()` to show sailing.

### Polymorphism

- All vehicles share the same method name (`move`) but behave differently when called.

## Example Code

```python
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
```

### Expected Output

```
Driving
Flying
Sailing
```

---

## Conclusion

This challenge shows how **polymorphism** allows different classes to implement the same method in unique ways.
Using polymorphism makes code flexible, reusable, and easier to extend with new classes in the future.
