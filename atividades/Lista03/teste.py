num = 12

num2 = num
cont = 1
while cont <= num2:
    num = cont
    if num > 1:    
        i = 2
        while i < num: 
            if (num % i) == 0:
                break
            i += 1
        else:
            print(f'{num} É PRIMO')
    cont += 1