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

1- mes  1268.25
"""

aplicacaoInicial = float(input('Digite a aplicação inicial: '))
taxaMensal = float(input('Digite a taxa de juros: ')) / 100

cont = 0
total = 0
while True:
    if cont == 0:
        limite = 12
        ...
    else:
        continuar = input('Deseja processar mais um ano? (S/N) ')
        if continuar in 'sS':
            limite += 12
            ...
        elif continuar in 'nN':
            break
        else:
            print('Opção inválida')
            continue
    
    while cont < limite:
        if cont == 0:
            taxa = aplicacaoInicial
        else:
            taxa += (taxa * taxaMensal)
        cont += 1
        total += taxa

    print(f'Rendimento mensal: {taxaMensal * 100}%')
    print(f'Saldo de investimento após {int(cont / 12)} ano(s): R${total:.2f}')