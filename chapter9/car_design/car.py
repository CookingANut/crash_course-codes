"""汽车类"""

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,miles):
        """将里程表读数增加到指定的量"""
        self.odometer_reading += miles


#my_new_car = Car('audi', 'a4', '2016')
#print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 13
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#my_used_car = Car('suabru', 'outback', 2013)
#print(my_used_car.get_descriptive_name())

#my_used_car.update_odometer(23500)
#my_used_car.read_odometer()

#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()