prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
prompt += "\nPlease input something: "
#message = ""

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
