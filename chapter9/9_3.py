class User():
    """初始化用户信息"""
    def __init__(self, s1, s2, s3, s4):
        self.first_name = s1
        self.last_name = s2
        self.age = s3
        self.address = s4
    
    def describe_user(self):
        """显示用户信息"""
        print("User info:")
        print("-Name: " + self.first_name + " " + self.last_name)
        print("-Age: " + str(self.age))
        print("-Address: " + self.address)
    
    def greet_user(self):
        print("Welcome, " + self.first_name + " " + self.last_name + ".\n")


#user1 = User("Yan", "lulu", 25, "Shenzhen, China")
#user2 = User ("Huang", "zhenfeng", 25, "Shenzhen, China")

#user1.describe_user()
#user1.greet_user()

#user2.describe_user()
#user2.greet_user()

user3 = User("Yan", "yan", 1, "changsha, Hunan")
user3.describe_user()

