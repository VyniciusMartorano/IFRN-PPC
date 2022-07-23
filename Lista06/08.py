import numpy as np
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

a = [l1, l2, l3]
print(f'{l1}\n{l2}\n{l3}')
print(f'Determinante: {int(np.linalg.det(a))}')