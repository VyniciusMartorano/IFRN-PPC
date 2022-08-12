import os
from functions import write_in_arq, readTable


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
            readTable(arq, full_text)


write_in_arq(f'{path}\dados_estatisticos\serie_historica_anp.txt', full_text)
                