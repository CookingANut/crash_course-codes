def city_info(city,country,population=0):
    if population == 0:
        info = city.title() + ',' + country.title()
    else:
        info = city.title() + ',' + country.title() + ' - ' + 'population ' + str(population)
    
    return(info)