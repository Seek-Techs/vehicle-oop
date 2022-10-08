class Vehicle:
    colour = 'white'
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity=50) -> None:
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


motto = Bus(34, 45)
print(motto.seating_capacity)