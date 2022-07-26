n = int(input('Informe um valor: '))
k = 1
base = n ** 2
while k <= base:
    termo1 = base // k
    termo2 = base % k
    k *= 10
    if n == 1:
        print('Número Kaprekar')
        break
    elif termo1 + termo2 == n and termo1 != 0 and termo2 != 0: #em algum momento, se a soma de termo1 e termo2 for igual a N
        print('Número Kaprekar')
        break
    elif termo1 + termo2 != n and k > base: 
        print('Não')
        break