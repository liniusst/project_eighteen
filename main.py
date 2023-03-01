# Lesson 19: OOP ( Part 2)

class Car:

    def get_car_color(self, color: str) -> None:
        print(f"My car color: {color}")

    def get_cost(self, cost: float) -> float:
        return cost
    
    def get_full_info(self, full_info: str) -> None:
        print(f"My full info: {full_info}")

class Ferrari(Car):
    SPEED_CONSTANTA = 20.5

    def __init__(self, hp: int) -> None:
        self.hp = hp

    def get_max_speed(self) -> float:
        return self.hp * self.SPEED_CONSTANTA
    
my_uber_car = Ferrari(hp= 450)
print(f"My max speed: {my_uber_car.get_max_speed()}")
my_uber_car.get_car_color("white")
