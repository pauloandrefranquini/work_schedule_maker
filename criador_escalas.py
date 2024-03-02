from tabulate import tabulate
import sys

data = []
col_names = []



class Funcionario:

    def __init__(self,nome):
        self.nome = nome
        self.primeira_folga = None
        self.lista = []


# Lista com meses do ano para poder modificar mais facilmente quantos dias tem a tabela e quantos dias de folga será
# gerada pela função.
meses_do_ano = {"Janeiro":31, "Fevereiro":29, "Março":31, "Abril":30, "Maio":31, "Junho":30,
                "Julho":31, "Agosto":31, "Setembro":30, "Outubro":31, "Novembro":30,
                 "Dezembro":31}




# Essa função adiciona o nome à lista e marca os dias de trabalho e de folga para poder ser usada
# pela biblioteca tabulate.

# Frequência é quantos dias o funcionário vai trabalhar para folgar
def dias_de_folga(frequencia, nome, mes):

    if nome.primeira_folga is None:
        nome.primeira_folga = frequencia
        nome.lista.append(nome.nome)
        return dias_de_folga(nome.primeira_folga, nome, mes)

    elif nome.primeira_folga >= 1 and len(nome.lista) < (meses_do_ano[mes]+1):
        for i in range(frequencia):
            if len(nome.lista) == (meses_do_ano[mes]+1):
                break
            else:
                nome.lista.append("o")
        for i in range(1):
            if len(nome.lista) == (meses_do_ano[mes]+1):
                break
            else:
                nome.lista.append("x")
        return dias_de_folga(nome.primeira_folga, nome, mes)


# Faz uma lista com os dias para poder ser usada pela biblioteca tabulate.
def nome_das_colunas(col_names, mes):
   col_names.append("Funcionários")
   for i in range(1,(meses_do_ano[mes] + 1)):
       col_names.append(i)


# Função para criar um objeto funcionário por meio de input
def add_funcionario(data,mes):
    funcionario = input("Qual o nome do funcionário? ")
    nome = Funcionario(funcionario)


    quantos_dias_de_trabalho = int(input("Quantos dias de serviço para um dia de folga? "))


    dias_de_folga(quantos_dias_de_trabalho, nome, mes)

    data.append(nome.lista)







def rodar_o_codigo(data, col_names):


        parar = input("Para criar uma tabela aperte 0, para parar o programa aperte 1: ")
        mes = input("Qual o mês corrente? ")

        if parar == "0":
            add_funcionario(data,mes)


            novo_funcionario = input( "Se você quer adicionar mais um funcionário aperte 0,"
                                      " para criar a tabela aperte 1:")

            if novo_funcionario == "0":
                add_funcionario(data,mes)
            elif novo_funcionario == "1":
                nome_das_colunas(col_names,mes)
                print(tabulate(data, headers=col_names, tablefmt="psql"))

        elif parar == "1":
            print("Programa finalizado")
            exit()








rodar_o_codigo(data, col_names)


