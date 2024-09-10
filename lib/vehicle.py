class Vehicle:

    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        print("vrrrrrrrooom!")
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        print("filling up!")
        return "filling up!"
    
mercedes = Vehicle(10,4)
mercedes.go()
mercedes.fill_up_tank()