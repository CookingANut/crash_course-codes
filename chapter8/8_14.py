def cars_info(manufacturer, model, **other_info):
    info = {}
    info['manufacturer'] = manufacturer
    info['model'] = model
    for key, value in other_info.items():
        info[key] = value
    return info


car1 = cars_info('subaru', 'outback', color = 'blue', tow_package = True)
car2 = cars_info('honda', 'accord', year=1991, color='white', headlights='popup')
print(car1)
print(car2)