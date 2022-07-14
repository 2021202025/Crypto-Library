import task1
import task2
import task3
import math


def xor(a, b):
    min_length = min(len(a), len(b))
    xor_message = ""
    for i in range(min_length):
        if a[i] == b[i]:
            xor_message += "0"
        else:
            xor_message += "1"

    return xor_message


def mac(k1, k2, message):
    n = len(k1)
    message_lis = []

    for i in range(math.ceil(len(message)/n)):
        mi = message[i*n:(i+1)*n]
        message_lis.append(mi)

    # tag = []
    # for i in range(len(k1)):
    #     tag.append('0')

    t = str(0)*n
    # print(t)

    for i in range(len(message_lis)):
        new_t = xor(t, message_lis[i])
        new_t = task2.pseduoRandFunc(k1, new_t)
        t = new_t

    t = task2.pseduoRandFunc(k2, t)

    return t


# k1 = input("Enter key 1: ")
# k2 = input("Enter key 2: ")

# message = input("Enter message: ")
# print(mac(k1, k2, message))
