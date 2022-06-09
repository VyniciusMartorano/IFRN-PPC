"""
Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês, sem usar a fórmula de juros compostos:

a. O programa deverá solicitar ao usuário o valor que será investido por mês e qual será o rendimento mensal;

b. O programa deve informar o saldo do investimento após um ano (soma das aplicações mês a mês considerando os juros compostos), e perguntar ao usuário se ele deseja que seja calculado o ano seguinte, sucessivamente;

c. Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha um rendimento de 1% ao mês, o programa forneceria a seguinte saída:

Valor inicial aplicado: R$ 100.00
Rendimento mensal: 1.00%
Saldo do investimento após 1 ano: R$ 1268.25
Deseja processar mais um ano? (S/N)

InvestimentoMensal
RendimentoMensal
"""
cont = 0
total = 0
cache = 0
aplicacaoInicial = 100
taxaMensal = 1 
while True:

    taxaMensal /= 100
    aplicacaoMensal = aplicacaoInicial

    if cont == 0:
        ...
        
    else:
        continuar = input('Deseja processar mais um ano? (S/N) ')
        if continuar in 'sS':
            cont = 0
            ...
        elif continuar in 'nN':
            break
        else:
            print('Opção inválida')
            continue

    while cont < 12:
        if cont == 0:
            total = aplicacaoInicial
        else:
            total += (total * taxaMensal)
        
        cont += 1
        cache += total
        print(total)

    print(f'Saldo de investimento após 1 ano: {cache}')
    
