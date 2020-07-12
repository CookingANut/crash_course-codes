"""冰淇淋小店类"""

from restaurant import Restaurant

class IceCreamstand(Restaurant):
    """初始化冰淇淋小店属性"""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavor(self):
        """显示冰淇淋的口味种类"""
        print("We have below flavor ice cream:")
        for flavor in self.flavors:
            print("- " + flavor)