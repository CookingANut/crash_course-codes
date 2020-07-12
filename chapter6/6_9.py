favorite_places={
    'lulu':['shanghai','chendu','xizhan'],
    'zhenf': ['shanghai'],
    'yanyan': ['hunan','haerbing'],
}

for name,places in favorite_places.items():
    print(name.title() + "'s favorite places:")
    for place in places:
        print(place)
    print("\n")