import json

def get_stored_username():
    """Get stored username if available."""
    filename = r'chapter10\w10_13\username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = r'chapter10\w10_13\username.json'
    with open(filename, 'w') as f_obj:   #以写入模式'w'打开文件，如果指定的文件已经存在，Python将在返回文件对象前清空该文件
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (if Yes type 'y'/if no type anything else) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
