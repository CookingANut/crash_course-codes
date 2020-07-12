sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiched = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiched.append(sandwich)

print("\nFinished sandwiched:")
for sandwiches in finished_sandwiched:
    print(sandwiches + " sandwich")
