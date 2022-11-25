text = input("Enter text: All uppercase or all lowercase:")


def ceasar(text):
    array = list(text)

    encryptedtext = []

    for character in array:
        integerValue = ord(character)
        if integerValue == 32:
            encryptedtext.append(chr(integerValue))
        else:
            integerValue -= 3
            if character.isupper():
                if integerValue < 65:
                    encryptedtext.append(chr(integerValue + 26))
                else:
                    encryptedtext.append(chr(integerValue))

            if character.islower():
                if integerValue < 97:
                    encryptedtext.append(chr(integerValue + 26))
                else:
                    encryptedtext.append(chr(integerValue))

    return "".join(encryptedtext)


print(ceasar(text))