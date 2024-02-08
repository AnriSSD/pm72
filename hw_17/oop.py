class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def age_of_car(self, current_year):
        return current_year - self.year

    @classmethod
    def total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def car_info(self):
        super().car_info()
        print(f"Battery life: {self.battery_life} hours")

    def battery_info(self):
        print(f"The battery life of this machine is {self.battery_life} hours")


# Example
car1 = Car("Toyota", "Prius", 2018)
car2 = Car("Honda", "Civic", 2020)

electric_car = ElectricCar("Tesla", "Model S", 2022, 300)
electric_car.car_info()
electric_car.battery_info()
print(f"Age of electric car: {electric_car.age_of_car(2024)} years")

Car.total_cars()

# display info abput every car
car1.car_info()
car2.car_info()
