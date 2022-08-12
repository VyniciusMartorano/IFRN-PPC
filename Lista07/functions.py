import os
from time import sleep

def write_in_arq(path: str, content: list) -> None:
    try:
        with open(path, 'w+') as file:
            for linha in content:
                value = ''
                for item in linha:
                    value += item + ';'
                value += '\n'
                file.write(value)
            file.close()

    except FileExistsError:
        ...
    else:
        print(f'O arquivo {path} foi escrito com sucesso')


def readTable(path: str, results: list):
    with open(path, 'r', encoding='utf-8') as file:
        file.readline()
        i = 0
        while True:
            i += 1
            try:
                line = file.readline()[:-1]
                if line == '':
                    break
                txt_splited = line.split(';')
                results.append(
                    [txt_splited[0], txt_splited[1], txt_splited[10],
                    txt_splited[11], txt_splited[12], txt_splited[14]]
                    )
                os.system('cls')
                print(i)
                
            except:
                ...
        print(f'O arquivo {path} foi lido com sucesso')
        file.close()