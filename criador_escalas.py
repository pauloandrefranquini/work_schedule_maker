from tabulate import tabulate
import time
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
meses_do_ano = {"JANEIRO":31, "FEVEREIRO":29, "MARÇO":31, "ABRIL":30, "MAIO":31, "JUNHO":30,
                "JULHO":31, "AGOSTO":31, "SETEMBRO":30, "OUTUBRO":31, "NOVEMBRO":30,
                 "DEZEMBRO":31}

# Esse código é utilizado para conseguir utilizar o mês atual para fazer a tabela
meses_do_ano_decimal= {1:"JANEIRO", 2:"FEVEREIRO", 3:"MARÇO", 4:"ABRIL", 5:"MAIO", 6:"JUNHO", 7:"JULHO", 8:"AGOSTO",
                       9:"SETEMBRO", 10:"OUTUBRO", 11:"NOVEMBRO", 12:"DEZEMBRO"}



# Essa função adiciona o nome à lista e marca os dias de trabalho e de folga para poder ser usada
# pela biblioteca tabulate.

# Frequência é quantos dias o funcionário vai trabalhar para folgar
def dias_de_folga(frequencia, nome, mes):
    try:
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
    except KeyError:
        print("Você escreveu o nome do mês de forma incorreta!")
        vai_para(data, col_names)


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



# Função para rodar o código e repetir, além de adicionar mais nomes à tabela conforme a vontade do usuário
# quando usuário quiser
def vai_para(data, col_names):
    parar = 0

    parar = input("Para criar uma tabela aperte 0, para parar o programa aperte 1: ")



    while int(parar) < 1:
        mes_atual= input("Utilizar mês atual para a tabela?[S/N]")

        if mes_atual == "S":
            time_object = time.localtime()

            local_time = time.strftime("%m",time_object)

            # Esse código é utilizado para conseguir utilizar o mês atual para fazer a tabela
            mes = (meses_do_ano_decimal[int(local_time)])

        else:
            mes = input("Qual o mês que você quer utilizar? ").upper()


        add_funcionario(data,mes)

        novo_funcionario = int(input("Se você quer adicionar mais um funcionário aperte 0,"
                                 " para criar a tabela aperte 1:"))

        while int(novo_funcionario) < 1:
            add_funcionario(data, mes)

            novo_funcionario = int(input("Se você quer adicionar mais um funcionário aperte 0,"
                                     " para criar a tabela aperte 1:"))

            if novo_funcionario == 0:
                pass
            else:
                novo_funcionario += 1

        nome_das_colunas(col_names, mes)
        print(tabulate(data, headers=col_names, tablefmt="psql"))



        parar = int(input("Quer fazer outra tabela ?[0 sim/1 não]"))

        if parar == 0:
            parar == 0
        else:
            parar += 1
            print("Programa Finalizado !!!")




vai_para(data, col_names)

# "data" são os dados para a tabela, enquanto os headers são os topos de cada tabela