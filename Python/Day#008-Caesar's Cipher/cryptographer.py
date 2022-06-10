class Cipher():
    """ Caeser's Cipher V1.0 Encrypt / Decrypt messages """

    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']

        self.msg = input("Please type your message below.\nYour message: ")
        self.job = input("encrypt or decrypt text? ")
        self.shift_amt = int(input("Shift message by how much?: "))

    def encrypt(self, text, shift):
        encrypted_text = ""
        for i in range(len(text)):
            if text[i] == " ":
                encrypted_text = encrypted_text + text[i]
            elif text[i] == "":
                encrypted_text = encrypted_text + chr((ord(text[i]) + shift) % 26 + 65)
            else:
                encrypted_text = encrypted_text + chr((ord(text[i]) + shift - 97) % 26 + 97)
        return encrypted_text

    def decrypt(self, encrypt_text, shift_amt):
        decrypted_text = ''
        for i in range(len(encrypt_text)):
            if encrypt_text[i] == ' ':
                decrypted_text = decrypted_text + encrypt_text[i]
            elif encrypt_text[i].isupper():
                decrypted_text = decrypted_text + chr((ord(encrypt_text[i]) - shift_amt - 65) % 26 + 65)
            else:
                decrypted_text = decrypted_text + chr((ord(encrypt_text[i]) - shift_amt - 97) % 26 + 97)
        return decrypted_text

    def works(self):
        if self.job.startswith('e'):
            print(self.encrypt(self.msg, self.shift_amt))

        elif self.job.startswith('d'):
            print(self.decrypt(self.msg, self.shift_amt))

        else:
            print("Thats not right try again!")