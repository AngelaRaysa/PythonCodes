class Car:
    def __init__(self, year_name, make):
        self.__year_name = year_name
        self.__make = make
        self.__speed = 0
     
    def accelerate(self):
        self.__speed = self.__speed + 5
     
    def brake(self):
        self.__speed = self.__speed - 5
    
    def get_speed(self):
        return self.__speed

def main():
    car = Car("2017", "Beamer")
    
    for i in range(5):
        car.accelerate()
        speed = car.get_speed()
        print("Current Speed:", speed)
    
    for i in range(5):
        car.brake()
        speed = car.get_speed()
        print("Current speed after brake:", speed)

main()
#123456789123456789123456789
#iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaam m m m m mbbbbbbbbbbbeeeeeessssssttttttt