def city_country(city_name, country_name):
    msg = "\n" + city_name.title() + ", " + country_name.title()
    return msg

message1 = city_country("shanghai","china")
print(message1)

message2 = city_country('华盛顿','美国')
print(message2)