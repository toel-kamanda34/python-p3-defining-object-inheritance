from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        print("VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!")
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
mercedes = Car(10,4)
mercedes.go()