variavel = '1234567890'
contPos = 0
contNeg = len(variavel)

while contPos < (len(variavel) * 2):
    if contPos <= len(variavel):
        print(variavel[0:contPos])
    else:
        print(variavel[0:contNeg])
    contPos += 1
    contNeg -= 1