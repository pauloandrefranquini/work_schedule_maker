from tabulate import tabulate

class Funcionario:

    def __init__(self,nome):
        self.nome = nome
        self.primeira_folga = None
        self.lista = []


# Essa função adiciona o nome à lista e marca os dias de trabalho e de folga para poder ser usada
# pela biblioteca tabulate.
def dias_de_folga(frequencia, funcionario):

    if funcionario.primeira_folga is None:
        funcionario.primeira_folga = frequencia
        funcionario.lista.append(funcionario.nome)
        return dias_de_folga(funcionario.primeira_folga, funcionario)

    elif funcionario.primeira_folga >= 1 and len(funcionario.lista) < 32:
        for i in range(frequencia):
            if len(funcionario.lista) == 32:
                break
            else:
                funcionario.lista.append("o")
        for i in range(1):
            if len(funcionario.lista) == 32:
                break
            else:
                funcionario.lista.append("x")
        return dias_de_folga(funcionario.primeira_folga, funcionario)


# Faz uma lista com os dias para poder usada pela biblioteca tabulate.
def nome_das_colunas(lista_col_nomes):
   for i in range(1,32):
       lista_col_nomes.append(i)


#teste
paulo = Funcionario("Paulo")
dias_de_folga(5, paulo)


roberto = Funcionario("Roberto")
dias_de_folga(4, roberto)

col_nomes = ["Funcionários"]
nome_das_colunas(col_nomes)


data = [paulo.lista, roberto.lista]


print(tabulate(data, headers= col_nomes))








