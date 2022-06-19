def get_cube(*args):
    for i in args:
        yield i ** 3

get_cube()

for i in get_cube(1,5,7):
    print(i)


def acronym_generator(listofword):
    for word in listofword:
        w1 = word.split()
        acr = ''
        for w in w1:
            acr += w[0].upper()
        yield acr

words = ['project manager','software engineer','database administrator']
for acr in acronym_generator(words):
    print(acr)