

text = input("Enter text:")

array = list(text)

encryptedText = []

for character in array:
    intall = ord(character)
    if intall == 108:
        encryptedText.append(chr(intall))
    else:
        intall -= 3
    encryptedText.append(chr(intall))