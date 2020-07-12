catsfile =r'chapter10/10_8/cats.txt'
dogsfile = r'chapter10/10_8/dogs.txt'

try:
    with open(catsfile) as c_obj:
        print('Cats name:')
        for line in c_obj:
            print('- ' + line.strip())
except FileNotFoundError:
    pass
    #print("No found " + catsfile)

try:
    with open(dogsfile) as d_obj:
        print('\nDogs name:')
        for line in d_obj:
            print('- ' + line.strip())
except FileNotFoundError:
    print("No found " + dogsfile)

