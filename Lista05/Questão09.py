variavel = '1234567890'
contNeg = len(variavel)

for i in range(len(variavel) * 2):
    if i <= len(variavel):
        print(variavel[0:i])
    else:
        print(variavel[0:contNeg])
    contNeg -= 1