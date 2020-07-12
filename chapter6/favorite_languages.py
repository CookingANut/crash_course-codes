favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

print("Sarah's favorite language is "+ favorite_languages['sarah'].title()+".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

print("\n")

#6.3.2
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("\tHi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + ".")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n")

print(favorite_languages.keys())  #keys()返回一个列表，其中包含字典所有的键
print("\n")

#6.3.3
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the pool.")

print("\n")

#6.3.4
print("The following languages have been mentioned:")
#for language in favorite_languages.values():
for language in set(favorite_languages.values()):   #让python找出列表中独一无二的元素，并且使用这些元素来创建一个集合
    print(language.title())


