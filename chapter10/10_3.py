guest_name = input('Please input your name?')

file_name = 'chapter10\guest.txt'

with open(file_name,'w') as file_object:
    file_object.write(guest_name)
