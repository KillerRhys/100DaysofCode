""" Caesar's Cipher
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.16-1914 """

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amt):
    encrypted_text = ""
    for i in range(len(plain_text)):
        if plain_text[i] == " ":
            encrypted_text = encrypted_text + plain_text[i]
        elif plain_text[i] == "":
            encrypted_text = encrypted_text + chr((ord(plain_text[i]) + shift_amt) % 26 + 65)
        else:
            encrypted_text = encrypted_text + chr((ord(plain_text[i]) + shift_amt - 97) %26 + 97)
    return encrypted_text


def decrypt(encrypt_text, shift_amt):
    decrypted_text = ''
    for i in range(len(encrypt_text)):
        if encrypt_text[i] == ' ':
            decrypted_text = decrypted_text + encrypt_text[i]
        elif encrypt_text[i].isupper():
            decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-shift_amt-65)%26+65)
        else:
            decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-shift_amt-97)%26+97)
    return decrypted_text


again_flag = True


def try_again():
    again = input("Use again?")
    again.lower()
    if again.startswith("y"):
        again_flag = True

    else:
        again_flag = False


while again_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(encrypt(text, shift))

    elif direction == "decode":
        print(decrypt(text, shift))

    else:
        print("I don't understand that let's try again...")