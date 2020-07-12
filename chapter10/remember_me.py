import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = r'chapter10\username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None  #返回空
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = r'chapter10\username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    
greet_user()