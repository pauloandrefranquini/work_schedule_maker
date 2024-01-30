from tabulate import tabulate

class Funcionario:

    def __init__(self,nome):
        self.nome = nome
        self.primeira_folga = None
        self.lista = []


def dias_de_folga(frequencia, funcionario):

    if funcionario.primeira_folga is None:
        funcionario.primeira_folga = frequencia
        funcionario.lista.append(funcionario.nome)
        return dias_de_folga(funcionario.primeira_folga, funcionario)

    elif funcionario.primeira_folga > 1 and len(funcionario.lista) < 31:
        for i in range(frequencia):
            funcionario.lista.append("o")
        for i in range(1):
            funcionario.lista.append("x")
        return dias_de_folga(funcionario.primeira_folga, funcionario)


def name_das_colunas(lista_col_nomes):
   for i in range(31):
       lista_col_nomes.append(i)


#teste
paulo = Funcionario("Paulo")
dias_de_folga(5, paulo)


roberto = Funcionario("Roberto")
dias_de_folga(4, roberto)

col_nomes = ["Funcionários"]
name_das_colunas(col_nomes)


data = [paulo.lista, roberto.lista]


print(tabulate(data, headers= col_nomes))








