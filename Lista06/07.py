from random import randint

l1 = []
l2 = []
l3 = []
for i in range(0, 3):
    n1 = randint(0, 9)
    n2 = randint(0, 9)
    n3 = randint(0, 9)
    l1.append(n1)
    l2.append(n2)
    l3.append(n3)
    
l1.append(l1[0])
l1.append(l1[1])

l2.append(l2[0])
l2.append(l2[1])

l3.append(l3[0])
l3.append(l3[1])

calcCima = (l3[0] * l2[1] * l1[2]) + (l3[1] * l2[2] * l1[3]) + (l3[2] * l2[3] * l1[4])
calcBaixo = (l1[0] * l2[1] * l3[2]) + (l1[1] * l2[2] * l3[3]) + (l1[2] * l2[3] * l3[4])
result =  calcBaixo - calcCima 


print(
f""""
{l1}
{l2}
{l3}
Determinante: {result}
""")