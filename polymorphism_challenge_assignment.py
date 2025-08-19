# Activity 2: Polymorphism Challenge

class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"


if __name__ == "__main__":
    # Demonstration of polymorphism
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(v.move())
