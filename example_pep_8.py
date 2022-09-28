# imports no TOP

import sys
import numpy
import pandas  # linhas separadas

from sqlite3 import Row, connect  # na mesma biblioteca os imports devem estar na mesma linha

# para múltiplos imports

from pandas import (
    array,
    DataFrame,
    Series,
    read_csv
)

"""
    Este é um exemplo de docstring

    Exemplificação sobre nomeação de recursos com python.
    tais recursos são: variáveis, classes, funções e espaçamento

    Editor do pycharm pode "reclamar" das palavras em português. Isso acarreta em avisos
    (linhas verdes) sobre as nomeações
    
    Os métodos e classes aqui podem não ser utilizados. São apenas para exemplificação da PEP 8

"""

# NAMING e Lines spacing


class Classe:
    pass

# functions


def soma():
    pass

# two spaces before a python class or method


class ClasseComposta:
    def __init__(self):
        inicio = 'Bem-vindo'
        return self.inicio
    pass


def function_compost():
    pass


def function_sum(number_one, number_two):
    """ Esta função retorna a soma de dois números """
    total = number_one + number_two
    return total


def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one


number = 4  # neste caso o python não reclama da nomeação (está em inglês)
numero_impar = 3 # devemos inserir dois espaços para iniciar um comentário


# Spaces between the function parameters
function_sum(2,3)
function_sum(2, 3)  # correct



# INDENTATION

"""
    A indentação é algo de grande importância no python. Ela determina toda a estrutura da
    aplicação. Sendo assim, podemos utilizar espaço ou tab. O mais frequentemente utilizado é o 
    espaço.
    
    A tecla TAB pode ser configurada de maneira diferente dependendo do sistema. Sendo assim, 
    utilizamos 4 espaços em detrimento do tab.
    
    Utilize sempre o mesmo método de identação
"""

if 2 in [1, 2.3, 4, 3, 5]:
    # dentro de uma estrutura os elementos devem ser separados por um espaço
    # [1,2.3,4,3,5] -> [1, 2.3, 4, 3, 5]
    print(True)


# ultima linha do código: linha em branco
