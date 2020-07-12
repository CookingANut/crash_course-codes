class Restaurant():
    """初始化酒店名和菜色"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """描述酒店信息"""
        print("This restaurant's name is " + self.restaurant_name + " and its cuisine type is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        """显示酒店营业中"""
        print("This restaurant " + self.restaurant_name + " is now opening.")


chinese_restaurant = Restaurant("Lulu's restaurant", "Chinese food")

print("This restaurant's name is " + chinese_restaurant.restaurant_name + ".")
print("This restayrant's cuisine type is " + chinese_restaurant.cuisine_type + ".")

chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()


