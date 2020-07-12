"""一个表示餐馆的类"""

class Restaurant():
    """初始化餐馆名和菜色"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """描述餐馆信息"""
        print("This restaurant's name is " + self.restaurant_name + " and its cuisine type is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        """显示餐馆营业中"""
        print("This restaurant " + self.restaurant_name + " is now opening.")
    
    def increment_number_served(self, daily_guests_avg):
        self.number_served += daily_guests_avg
