users_list=[]
#users_list=['admin','david','michael','jordan','ken']
user_name='admin'

if users_list:
    if user_name=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+user_name+", thank you for logging in again.")
else:
    print("We need to find some users!")

