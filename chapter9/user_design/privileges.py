"""管理员权限类"""

class Privileges():
    def __init__(self):
        self.privileges =  [
            "can add post", 
            "can delete post", 
            "can ban user"
            ]
    
    def show_privileges(self):
        print("\nThe administrator has below privileges:")
        for privilege in self.privileges:
            print("- " + privilege)