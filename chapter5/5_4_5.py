#alien_color='yellow'
alien_color='green'
#alien_color='red'

if alien_color=="green":
    point=5
elif alien_color=="yellow":
    point=10
elif alien_color=="red":
    point=15

print("\nPlayer get "+str(point)+" points because of shooting "+alien_color+" alien!\n")