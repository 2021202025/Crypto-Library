import task1


def g0(k):
    new_k = task1.g_calc(k)
    # print("g0:", new_k)
    return new_k[:len(k)]


def g1(k):
    new_k = task1.g_calc(k)
    # print("g1:", new_k)
    return new_k[len(new_k)//2:len(new_k)//2+len(k)]


def xor(a, b):
    min_length = min(len(a), len(b))
    xor_message = ""
    for i in range(min_length):
        if a[i] == b[i]:
            xor_message += "0"
        else:
            xor_message += "1"

    return xor_message


def pseduoRandFunc(key, input):
    # r = task1.g_calc(seed)[:len(message)]
    # print(r)
    encr = key
    for i in input:
        # print(encr)
        if i == '0':
            encr = g0(encr)
        else:
            encr = g1(encr)

    # print("Enc ", encr)

    # encr = xor(encr, message)
    return encr


# key = input("Enter key in binary: ")
# message = input("Enter input for prf: ")

# prf_ouput = pseduoRandFunc(key, message)
# print(prf_ouput)
