from math import sqrt



def bhaskara(ax, bx, c):
    delta = bx**2 -4 * ax * c

    if delta < 0:
        return 'Delta menor que zero'

    x1 = (- bx + sqrt(delta)) / (2*ax)
    x2 = (-bx - sqrt(delta)) / (2*ax)

    if delta == 0:
        return f'({x1:.2f})'
    
    return f'({x1:.2f},{x2:.2f})'


print(bhaskara(5, -8, 7))

