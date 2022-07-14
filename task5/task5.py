import task1
import task2
import task3_task5
import task4
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


def encrypt(k1, k2, IV, message):
    encrypted_message = task3_task5.cbc_prf(IV, k1, message)
    mac = task4.mac(k1, k2, encrypted_message[0])
    cipher_text = encrypted_message[0] + " " + mac
    return cipher_text


def decrypt(k1, k2, n, cipher_text):
    text_blocks = cipher_text.split(" ")
    encrypted_message = text_blocks[0]
    mac = text_blocks[1]

    pt = task3_task5.decrypt(n, k1, encrypted_message)
    print(pt)
    calculated_mac = task4.mac(k1, k2, encrypted_message)
    # print(calculated_mac)

    if mac == calculated_mac:
        print("Message is authentic")
    else:
        print("Message is not authentic")

    # return actual_text


k1 = input("Enter key 1: ")
k2 = input("Enter key 2: ")
IV = input("Enter IV: ")
message = input("Enter message: ")

cipher_text = encrypt(k1, k2, IV, message)
# print(cipher_text)

decrypt(k1, k2, len(IV), cipher_text)
# print(actual_text)
