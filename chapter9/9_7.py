class User():
    """初始化用户信息"""
    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.login_attempts = 0
    
    def describe_user(self):
        """显示用户信息"""
        print("User info:")
        print("-Name: " + self.first_name + " " + self.last_name)
        print("-Age: " + str(self.age))
        print("-Address: " + self.address)
    
    def greet_user(self):
        """显示一条问候语"""
        print("Welcome, " + self.first_name + " " + self.last_name + ".\n")
    
    def increment_login_attempts(self):
        """将登入次数加1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """将登入次数重置为0"""
        self.login_attempts = 0


class Admin(User):
    """设置管理员属性"""
    def __init__(self, first_name, last_name, age, address):
        super().__init__(first_name, last_name, age, address)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        """显示管理员权限"""
        print("Administrator has below privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

first_admin = Admin("Yan","lulu", 25, "shenzhen China")
first_admin.describe_user()
first_admin.show_privileges()
 