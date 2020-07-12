filename = 'chapter10\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print('Your birthday appears in the first million digits of Pi!')
else:
    print("You birthday does not appears in the million digits of Pi.")



#print(pi_string[:52] + "...")
#print(pi_string)

