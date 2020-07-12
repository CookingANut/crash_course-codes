alien_0={'color':'green','point':5}

print(alien_0['color'])
print(alien_0['point'])

new_points=alien_0['point']
print('You just earned '+str(new_points)+" points!")

del alien_0['point']
print(alien_0)