import task1

g = 163
q = 37537

bin_g = bin(g).replace('0b', '')
h = task1.g_calc(bin_g)
h = int(h, 2)


def calculate_hash(x1, x2):

    fixed_hash = (pow(g, x1, q) * pow(h, x2, q)) % q
    bin_fixed_hash = bin(fixed_hash).replace('0b', '')
    # print(fixed_hash)
    bin_fixed_hash = bin_fixed_hash.zfill(16)
    return bin_fixed_hash


x1 = int(input("Enter x1(< 37537): "))
x2 = int(input("Enter x2(< 37537): "))

hashed = calculate_hash(x1, x2)
print(hashed, len(hashed))
