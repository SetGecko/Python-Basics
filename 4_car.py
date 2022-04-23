class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.name} {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} превышает допустимую скорость")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} превышает допустимую скорость")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar(70, "черная", "Ford", False)
sport_car = SportCar(180, "красная", "F1", False)
work_car = WorkCar(30, "белая", "Audi", False)
police_car = PoliceCar(90, "синяя", "VAZ", True)

town_car.go()
town_car.show_speed()
town_car.stop()

sport_car.go()
sport_car.show_speed()
sport_car.turn("направо")
sport_car.stop()
