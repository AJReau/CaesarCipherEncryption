# Caesar Encryption Program
# Objective is to ask the user if they want to encode or decode a message using Caesar encryption method


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Will ask user for their message to encrypt as well as the shift amount
def encrypt(plainText, shiftAmount):
    encodedText = ""
    for letter in plainText:
        if alphabet.index(letter) + shiftAmount > len(alphabet):
            encodedText += alphabet[alphabet.index(letter) + shiftAmount - len(alphabet)]
        else:
            encodedText += alphabet[alphabet.index(letter) + shiftAmount]
    print(encodedText)


# Decrypts a text using the inputted message and the shift key
def decrypt(plainText, shiftAmount):
    decryptedText = ""
    for letter in plainText:
        if alphabet.index(letter) - shiftAmount < 0:
            decryptedText += alphabet[alphabet.index(letter) - shiftAmount + len(alphabet)]
        else:
            decryptedText += alphabet[alphabet.index(letter) - shiftAmount]
    print(decryptedText)


# Determines what mode the user is in
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("You did not enter encode or decode")
