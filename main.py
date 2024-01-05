#
with open("relatorio.txt", "r", encoding='utf-8') as arquivo:
    dados = arquivo.read().replace('.', '').replace(',', '.').split()

posicoes = [indice for indice, elemento in enumerate(dados) if elemento == 'venda:']

total_vendas = [dados[indice + 2] for indice in posicoes]

valor_mao_de_obra = [dados[indice - 6] for indice in posicoes]

mecanico = [dados[indice - 10] for indice in posicoes]

"""print(f'Total de Vendas: {total_vendas}\n')
print(f'Valor da Mão de Obra: {valor_mao_de_obra}\n')
print(f'Mecânico: {mecanico}\n')"""

filtragem = list(zip(mecanico, valor_mao_de_obra, total_vendas))
"""print(filtragem)"""

carlos = []
antonio = []
pedro = []
gabriel = []
sebastiao = []
lucas = []
ricardo = []
marcelo = []


def separar_mecanicos(nome, lista):
    for item in filtragem:
        if item[0] == nome:
            lista.append(item)


separar_mecanicos('CARLOS', carlos), separar_mecanicos('ANTONIO', antonio)
separar_mecanicos('PEDRO', pedro), separar_mecanicos('GABRIEL', gabriel)
separar_mecanicos('SEBASTIAO', sebastiao), separar_mecanicos('LUCAS', lucas)
separar_mecanicos('RICARDO', ricardo), separar_mecanicos('MARCELO', marcelo)

print()
#print(f'CARLOS: {carlos}\n ANTONIO; {antonio}\n PEDRO: {pedro}\n GABRIEL: {gabriel}\n'
#      f' SEBASTIAO: {sebastiao}\n LUCAS: {lucas}\n RICARDO: {ricardo}\n MARCELO: {marcelo}\n')

vendas_carlos = []
vendas_antonio = []
vendas_pedro = []
vendas_gabriel = []
vendas_sebastiao = []
vendas_lucas = []
vendas_ricardo = []
vendas_marcelo = []


def subtrair_valores(lista, vendas_mecanico):
    for item in lista:
        subtracao = float(item[2]) - float(item[1])
        vendas_mecanico.append(subtracao)


subtrair_valores(carlos, vendas_carlos)
subtrair_valores(antonio, vendas_antonio)
subtrair_valores(pedro, vendas_pedro)
subtrair_valores(gabriel, vendas_gabriel)
subtrair_valores(sebastiao, vendas_sebastiao)
subtrair_valores(lucas, vendas_lucas)
subtrair_valores(ricardo, vendas_ricardo)
subtrair_valores(marcelo, vendas_marcelo)

print(f'Total de vendas por MECÂNICO: \n')


def somar_formatar(nome, vendas_mecanico):
    soma = (sum(vendas_mecanico))
    print(f'{nome}{soma:,.2f}'.replace(',', '.'))


resultado_carlos = somar_formatar('CARLOS = ', vendas_carlos)
resultado_antonio = somar_formatar('ANTONIO = ', vendas_antonio)
resultado_pedro = somar_formatar('PEDRO = ', vendas_pedro)
resultado_gabriel = somar_formatar('GABRIEL = ', vendas_gabriel)
resultado_sebastiao = somar_formatar('SEBASTIAO = ', vendas_sebastiao)
resultado_lucas = somar_formatar('LUCAS = ', vendas_lucas)
resultado_ricardo = somar_formatar('RICARDO = ', vendas_ricardo)
resultado_marcelo = somar_formatar('MARCELO  = ', vendas_marcelo)
