import car
import electric_car

my_beetle = car.Car('volkswagen', 'beetle', '2016')
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())