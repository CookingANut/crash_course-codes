current_users=['jack','ken','nan','jane','fox']
new_users=['JACK','KEN','david','feng','jam']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You are not able to use this name ("+new_user+"), please another user name.")
    else:
        print("congradulation! This users name is not been used.")