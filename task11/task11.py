import math
import random
import string
import prg
import task7
import task6_task7


def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return x


# e needs to be co prime with N and Phi_N
def get_encryption_key(N, phi_N):
    possible_e = []
    for i in range(1, N+1):
        if (1 < i) and (i < phi_N):
            gcd = computeGCD(i, N)
            gcd_phi = computeGCD(i, phi_N)
            if (gcd == 1) and (gcd_phi == 1):
                # return i
                possible_e.append(i)
    if len(possible_e) > 1:
        return possible_e[random.randint(1, len(possible_e)-1)]
    else:
        return possible_e[0]


# choose d such that d*e mod phi_N = 1
def get_decryption_key(e, phi_N):
    possible_d = []
    for i in range(e * 25):
        if (e * i) % phi_N == 1:
            possible_d.append(i)
    if len(possible_d) > 1:
        return possible_d[random.randint(1, len(possible_d)-1)]
    else:
        return possible_d[0]
    # return possible_d[random.randint(1, len(possible_d) - 1)]


def text_to_digits(message):
    pool = string.ascii_letters + string.punctuation + " "
    # print(pool)
    M = []
    for i in message:
        M.append(pool.index(i))
    return M


def digits_to_text(message_digest):
    pool = string.ascii_letters + string.punctuation + " "
    msg = ''
    for i in message_digest:
        msg += pool[i]
    return msg


def encrypt(M, public_key):
    # print(M)
    return [(i ** public_key[0]) % public_key[1] for i in M]


def encrypt_hash(hash_message, private_key):
    int_message = (int(hash_message, 2) % private_key[1])
    # print(int_message)
    y = ((int_message ** private_key[0]) % private_key[1])

    return y

    # print(int_message)


def decrypt(CT, private_key):
    # print(CT)
    return [((i ** private_key[0]) % private_key[1]) for i in CT]


def decrypt_hash(enc_hash, public_key):
    # int_message = int(message, 2)
    return ((enc_hash ** public_key[0]) % public_key[1])


def message_to_binary(message_lis):
    binary_message = ""
    for i in message_lis:
        binary_message += bin(i).replace('0b', '').zfill(32)
    # print(len(binary_message))
    return binary_message


def message_to_binary8bit(message_lis):
    binary_message = ""
    for i in message_lis:
        binary_message += bin(i).replace('0b', '').zfill(8)
    # print(len(binary_message))
    return binary_message


def pad_rsa(fixed_bytes, binary_r, null_byte, binary_message):
    return fixed_bytes + binary_r + null_byte + binary_message


def remove_pad_rsa(cipher_text):
    message_lis = []
    n = len(cipher_text)//8
    for i in range(n):
        message_lis.append(int(cipher_text[i*8:i*8+8], 2))

    # print(message_lis)
    count = 0
    for i in message_lis:
        count += 1
        # print(count)
        if i == 0:
            break

    message_lis = message_lis[count:]
    encrypted_binary = message_to_binary8bit(message_lis)
    # print(encrypted_binary)

    message_lis = []
    n = len(encrypted_binary)//32
    # print(len(encrypted_binary))
    for i in range(n):
        # print(i)
        message_lis.append(int(encrypted_binary[i*32:i*32+32], 2))

    # print(message_lis)
    return message_lis


p = 41
q = 59

# Public key N,e
N = p * q
phi_N = (p - 1) * (q - 1)
# print(N)
# print(phi_N)
e = get_encryption_key(N, phi_N)
# print(e)
d = get_decryption_key(e, phi_N)
# print(d)

while d == e:
    d = get_decryption_key(e, phi_N)

public_key = [e, N]
private_key = [d, N]

null_byte = "00000000"

# print(prg.g_calc("011111001000111101001011000100011111100010011011"))
fixed_bytes = "0101001111011010"
binary_r = "0101001111011010011111001000111101001011000100011111100010011011"
# binary_r = message_to_binary(r)
# print(len(binary_r))
# message length should be less than 1014 bytes
# message = input("Enter the message to be encrypted: ")
message = input("Enter the message to be encrypted (a string like 'dog'): ")
parsed_message = text_to_digits(message)
cipher_text = encrypt(parsed_message, public_key)
binary_cipher = message_to_binary(cipher_text)
cipher_to_send = pad_rsa(fixed_bytes, binary_r, null_byte, binary_cipher)

hash_message = message_to_binary(parsed_message)
hashed = task7.calculate_hash(16, "1010111110101111", hash_message)
encrypted_hash = encrypt_hash(hashed, private_key)
# print(encrypted_hash)
initial_hash_message = (int(hashed, 2) % private_key[1])
# print(initial_hash_message)
cipher_to_send = cipher_to_send + " " + str(encrypted_hash)

# print(cipher_to_send)
# print(cipher_text)
# print(binary_cipher)


pad_removed_cipher = remove_pad_rsa(cipher_to_send)
# print(cipher_text)
decrypted_text = decrypt(pad_removed_cipher, private_key)
decrypted_hash = decrypt_hash(encrypted_hash, public_key)
decrypted_message = digits_to_text(decrypted_text)


print()
print("Message ->", message, end="\n\n")
print("Parsed Message ->", parsed_message,  end="\n\n")
print("Encrypted Message ->", cipher_text,  end="\n\n")
# print(decrypted_text,  end="\n\n")
print("Decrypted Message ->", decrypted_message,  end="\n\n")

print("Original Hash ->", initial_hash_message, end="\n\n")
print("Decrypted Hash ->", decrypted_hash, end="\n\n")

if(decrypted_hash == initial_hash_message):
    print("Message is authentic")
else:
    print("Message is not authentic")
