def dectobin(nb):
    r = []

    while(nb>0):
        r.append(nb%2)
        nb = nb // 2

    return ''.join(str(i) for i in r[::-1])

def bintodec(nb):
    n = [int(i) for i in nb[::-1]]
    r = 0

    for i in range(0,len(n)):
        r += n[i] * 2**i

    return r

nb = 2

# binaire = dectobin(nb)
# print(binaire)

# decimal = bintodec(binaire)
# print(decimal)
