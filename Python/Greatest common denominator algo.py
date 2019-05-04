


def gcd (a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a



print(gcd(55, 4))
print(gcd(22, 4))
print(gcd(60, 96))
