def gcd():
    a, b, tmp

    a = value1
    b = value2

    if (a < 0):
    	a = -a

    if (b < 0):
        b = -b

    if (a == 0 | b == 0):
        print("The input values must be greater than zero\n")
        return

    while (b > 0):
        tmp = a % b
        a = b
        b = tmp

    print("Result: %i\n", a)
