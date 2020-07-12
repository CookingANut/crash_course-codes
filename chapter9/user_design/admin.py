"""管理员类"""

import user
import privileges

class Admin(user.User):
    """设置管理员属性"""
    def __init__(self, first_name, last_name, age, address):
        super().__init__(first_name, last_name, age, address)
        self.privileges = privileges.Privileges()
    
    def describe_user(self):
        """显示管理员信息"""
        print("Admin info:")
        print("- Name: " + self.first_name + " " + self.last_name)
        print("- Age: " + str(self.age))
        print("- Address: " + self.address)
