g = 163
p = 37537


def generator(g, x, p):
    return pow(g, x, p)


def alice(x, h2):
    # print(h2)
    kA = pow(h2, x, p)
    print(kA)


def bob(y, h1):
    # print(h1)
    kB = pow(h1, y, p)
    print(kB)


def key_exhcange(x, y):
    h1 = generator(g, x, p)
    h2 = generator(g, y, p)
    print(h1, h2)
    alice(x, h2)
    bob(y, h1)


x = int(input("Enter x < 37537: "))
y = int(input("Enter y < 37537: "))


key_exhcange(x, y)
