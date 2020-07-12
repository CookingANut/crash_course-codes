sandwich_orders = [
    'pastrami',
    'veggie',
    'grilled cheese',
    'turkey',
    'pastrami',
    'roast beef',
    'pastrami',
    ]

print("We havd sold out the pastrami sandwich.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("Sandwich orders: ")
for sandwiches in sandwich_orders:
    print(sandwiches + " sandwich")