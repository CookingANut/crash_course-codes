rivers={
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china'
}

for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThe countries that runs through include:")
for country in sorted(set(rivers.values())):
    print(country.title())