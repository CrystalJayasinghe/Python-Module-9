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
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def output(self):
        print(f"Registration_number: {self.registration_number}\n" 
              f"maximum_speed: {self.maximum_speed}\n" 
              f"current_speed: {self.current_speed}\n"
              f"travelled_distance: {self.travelled_distance}")


car = Car("ABC-123", 142)



car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Current speed after acceleration: {car.current_speed}km/h")

car.accelerate(-200)
print(f"Current speed after brakes: {car.current_speed}km/h")



