class Vehicle:
    colour = 'white'
    fare = 100
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
        Vehicle.fare
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=50) -> None:
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def fare(self):
        return seating_capacity*Vehicle.fare

class Bus(Vehicle):
    pass
motto = Bus(max_speed=34, mileage=45)
print(motto.fare)