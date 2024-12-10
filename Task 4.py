import random
from tabulate import tabulate


class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        return distance


car1 = Car("ABC-1", random.randint(100, 200))
car2 = Car("ABC-2", random.randint(100, 200))
hours = 0
while car1.travelled_distance < 10000 and car2.travelled_distance < 10000:
    hours += 1
    if car1.current_speed < car1.maximum_speed:
        car1.accelerate(random.randint(10, 15))
    if car2.current_speed < car2.maximum_speed:
        car2.accelerate(random.randint(10, 15))
    car1.travelled_distance += car1.drive(1)
    car2.travelled_distance += car2.drive(1)


print(tabulate([['car1', car1.registration_number, car1.current_speed, car1.travelled_distance, car1.maximum_speed],
               ['car2', car2.registration_number, car2.current_speed, car2.travelled_distance, car2.maximum_speed]],
               headers=['car', 'registration_number', 'current_speed', 'travelled_distance', 'maximum_speed']))
