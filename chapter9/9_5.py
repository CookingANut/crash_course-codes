class User():
    """初始化用户信息"""
    def __init__(self, s1, s2, s3, s4):
        self.first_name = s1
        self.last_name = s2
        self.age = s3
        self.address = s4
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


user1 = User("Yan", "lulu", 25, "Shenzhen, China")

for times in range(15):
    user1.increment_login_attempts()

print("Login attempts: " + str(user1.login_attempts))

user1.reset_login_attempts()
print("Login attempts: " + str(user1.login_attempts))

