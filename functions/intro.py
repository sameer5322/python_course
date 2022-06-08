# program that finds the hypotenuse

#p = float(input("Enter the lenght of first side: "))
#b = float(input("Enter the lenght of second side: "))

#h = (p**2 + b**2)**0.5
#print('Perpendicular:',p)
#print('Base:',b)
#print('The Hypotenuse is:',h)

# fuctions are defined using 'def' keyword
# and the we can use these defined function by calling them
def hypotenuse():
    p = float(input("Enter the lenght of first side: "))
    b = float(input("Enter the lenght of second side: "))

    h = (p**2 + b**2)**0.5
    print('Perpendicular:',p)
    print('Base:',b)
    print('The Hypotenuse is:',h)

# calling
hypotenuse()