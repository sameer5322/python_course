def check_prime():
    a = 541
    for i in range(2,541):
        if a%i == 0:
            return('not prime')
    else:
        return('prime')

out = check_prime()
print(out)