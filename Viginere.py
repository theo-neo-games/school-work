def ValidateItem(input_parameter):
    try:
        if -100 <= input_parameter <= 100:
            return True
    except ValueError:
        return False


plainText = input('Input the plaintext: ').upper()

keyword = input('Input the keyword: ').upper()


keywordList = []
keywordLength = len(keyword)
for l in range(keywordLength):
    keywordList.append(ord(keyword[l]) - 65)


asciiPlaintext = []

plainTextLength = len(plainText)

for i in range(plainTextLength):
    asciiPlaintext.append(ord(plainText[i]))

keywordIndex = 0
for j in range(plainTextLength):
    if plainText[j] == ' ':
        asciiPlaintext[j] = ' '
    else:
        asciiPlaintext[j] += keywordList[keywordIndex]
        while True:
            if asciiPlaintext[j] < 65:
                asciiPlaintext[j] += 26
            elif asciiPlaintext[j] > 90:
                asciiPlaintext[j] -= 26
            else:
                break
        asciiPlaintext[j] = chr(asciiPlaintext[j])
        keywordIndex += 1
        if keywordIndex >= keywordLength:
            keywordIndex = 0

cipherText = ''
for k in range(plainTextLength):
    cipherText += asciiPlaintext[k]

print(cipherText)