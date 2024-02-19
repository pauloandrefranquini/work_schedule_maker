from tabulate import tabulate

class Funcionario:

    def __init__(self,nome):
        self.nome = nome
        self.primeira_folga = None
        self.lista = []


# Lista com meses do ano para poder modificar mais facilmente quantos dias tem a tabela e quantos dias de folga será
# gerada pela função.
meses_do_ano = {"Janeiro":31, "Fevereiro":28, "Março":31, "Abril":30, "Maio":31, "Junho":30,
                "Julho":31, "Agosto":31, "Setembro":30, "Outubro":31, "Novembro":30,
                 "Dezembro":31}




# Essa função adiciona o nome à lista e marca os dias de trabalho e de folga para poder ser usada
# pela biblioteca tabulate.

# Frequência é quantos dias o funcionário vai trabalhar para folgar
def dias_de_folga(frequencia, funcionario, mes):

    if funcionario.primeira_folga is None:
        funcionario.primeira_folga = frequencia
        funcionario.lista.append(funcionario.nome)
        return dias_de_folga(funcionario.primeira_folga, funcionario, mes)

    elif funcionario.primeira_folga >= 1 and len(funcionario.lista) < (mes + 1):
        for i in range(frequencia):
            if len(funcionario.lista) == (mes + 1):
                break
            else:
                funcionario.lista.append("o")
        for i in range(1):
            if len(funcionario.lista) == (mes + 1):
                break
            else:
                funcionario.lista.append("x")
        return dias_de_folga(funcionario.primeira_folga, funcionario, mes)


# Faz uma lista com os dias para poder ser usada pela biblioteca tabulate.
def nome_das_colunas(lista_col_nomes, mes):
   for i in range(1,(mes + 1)):
       lista_col_nomes.append(i)


#teste
paulo = Funcionario("Paulo")
dias_de_folga(5, paulo, meses_do_ano["Fevereiro"])


roberto = Funcionario("Roberto")
dias_de_folga(4, roberto, meses_do_ano["Fevereiro"])

col_nomes = ["Funcionários"]
nome_das_colunas(col_nomes, meses_do_ano["Fevereiro"])


data = [paulo.lista, roberto.lista]


print(tabulate(data, headers= col_nomes, tablefmt="psql"))








