class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=2000):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance
        return self.travelled_distance

    def output(self):
        print(f"Registration_number: {self.registration_number}\n" 
              f"maximum_speed: {self.maximum_speed}\n" 
              f"current_speed: {self.current_speed}\n"
              f"travelled_distance: {self.travelled_distance}")


car = Car("ABC-123", 142)



car.accelerate(60)
print(car.current_speed)
print(car.drive(1.5))
