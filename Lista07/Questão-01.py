import os
import csv


path = os.path.dirname(__file__)
full_text = []

os.system('cls')

try:
    os.mkdir(path + '\dados_estatisticos')
except FileExistsError:
    ...

for root, sp, arqs in os.walk(path):
    for arq in arqs:
        ext = os.path.splitext(arq)[1]
        if ext == '.csv':
            with open(arq, 'r', encoding='utf-8') as file:
                file.readline()
                while True:
                    try:
                        line = file.readline()[:-1]
                        if line == '':
                            break
                        txt_splited = line.split(';')
                        full_text.append(
                            [txt_splited[0], txt_splited[1], txt_splited[10],
                            txt_splited[11], txt_splited[12], txt_splited[14]]
                            )
                    except:
                        ...
                file.close()


try:
    with open(f'{path}\dados_estatisticos\serie_historica_anp.txt', 'w+') as file:
        for linha in full_text:
            value = ''
            for item in linha:
                value += item + ';'
            value += '\n'
            file.write(value)
        file.close()
except FileExistsError:
    ...
                

#posições
# 0, 1, 10, 11, 12, 14

