import random

def say_hello():
    msg = ['Hello','Namaste','Hola','Bonjour','Guten Tag']   # gives random element everytime
    print(random.choice(msg))



say_hello()
say_hello()
say_hello()
say_hello()