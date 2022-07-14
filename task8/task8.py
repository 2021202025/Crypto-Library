import task6_task7
import task7_task8
import math

ipad = '00110110'
opad = '01011100'


def xor(a, b):
    min_length = min(len(a), len(b))
    xor_message = ""
    for i in range(min_length):
        if a[i] == b[i]:
            xor_message += "0"
        else:
            xor_message += "1"

    return xor_message


def calculate_hmac(n, IV, k, message):
    # Assuming n to always be a multiple of 8
    # print(len(message))
    times = n//8

    new_ipad = ""
    new_opad = ""
    for i in range(times):
        new_ipad += ipad
        new_opad += opad

    # print(new_ipad, len(new_ipad))
    # print(new_opad, len(new_opad))

    k_xor_ipad = xor(k, new_ipad)
    k_xor_opad = xor(k, new_opad)

    # print(k_xor_ipad)

    message = k_xor_ipad + message

    ipad_hash = task7_task8.calculate_hash(n, IV, message)
    # print(ipad_hash)

    opad_hash = task6_task7.calculate_hash(int(k_xor_opad, 2), int(IV, 2))
    # print(opad_hash)

    HMAC_tag = task6_task7.calculate_hash(int(ipad_hash, 2), int(opad_hash, 2))

    return HMAC_tag


n = int(input("Enter fixed hash length: "))
IV = input("Enter Initialization Vector: ")
k = input("Enter key: ")
message = input("Enter message: ")

tag = calculate_hmac(n, IV, k, message)
print(tag)