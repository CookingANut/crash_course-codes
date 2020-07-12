favorite_languages={
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edwars': ['ruby', 'go'],
    'phil': ['python','haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())