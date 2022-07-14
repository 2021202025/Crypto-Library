import task1
import task2
import math


def g0(k):
    new_k = task1.g_calc(k)
    # print(new_k)
    return new_k[:len(k)]


def g1(k):
    new_k = task1.g_calc(k)
    # print(new_k)
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


def encrypt(IV, key, message_blocks):
    encrypted_text = IV

    for i in range(len(message_blocks)):
        IV = bin(int(IV, 2) + 1).replace("0b", "")
        # print(IV)
        randomized_IV = task2.pseduoRandFunc(key, IV)
        # print(IV, randomized_IV)
        ci = xor(message_blocks[i], randomized_IV)
        # print(ci)
        encrypted_text += ci

    # print(encrypted_text)
    return encrypted_text


def decrypt(IV_len, key, cipher_text):
    IV = cipher_text[:IV_len]
    cipher_text = cipher_text[IV_len:]

    no_of_blocks = math.ceil(len(cipher_text) / IV_len)
    n = IV_len

    message_lis = []
    for i in range(no_of_blocks):
        mi = cipher_text[i*n:(i+1)*n]
        message_lis.append(mi)

    plain_text = ""

    for i in range(len(message_lis)):
        IV = bin(int(IV, 2) + 1).replace("0b", "")
        randomized_IV = task2.pseduoRandFunc(key, IV)
        pi = xor(message_lis[i], randomized_IV)
        plain_text += pi

    return plain_text


def cbc_prf(IV, key, message):
    n = len(IV)
    no_of_blocks = math.ceil(len(message) / n)

    message_lis = []
    # print(message)
    for i in range(no_of_blocks):
        mi = message[i*n:(i+1)*n]
        message_lis.append(mi)

    cipher_text = encrypt(IV, key, message_lis)
    actual_text = decrypt(n, key, cipher_text)

    print("Encrypted: ", cipher_text)
    print("Decrypted: ", actual_text)


# initialization vector for Cipher Block Chaining
initial_seed = input("Enter initialization vector for CBC: ")
key = input("Enter key (same length as IV): ")
message = input("Enter user message in binary (any length): ")

cbc_prf(initial_seed, key, message)
