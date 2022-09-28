"""
    Isto é uma docstring
"""

'''
    Isso é uma docstring
'''
# Treinando a PEP 8
# ctrl + alt + l -> organiza a identação do código

# errado
import sys, os

# correto
import pandas
import matplotlib
import numpy

from pandas import array
# quebra de linha para múltiplos imports
from pandas import (
        read_csv,
        Series,
        DataFrame,
        HDFStore
)

# from caminho import function, ClasseEspecifica


# Constantes
CONSTANT = 100


# classe
class JuridicPerson:
    # classes começam por letra maiscula
    def __init__(self, message):
        self.name = None
        self.email = None
        self.inicio = message
    pass

    # nome é separado por underline
    def set_name(self, name):
        """
            Este método tem por objetivo setar o nome do objeto
        instanciado pela classe.

        :param name: o nome definido pelo usuário
        :return: self.name
        """
        self.name = name
        print('O nome é: ', name)
        return self.name


variaveis = 0
x =1
y=2

lista = [1,2,3,4,5,6,7,8,9]  # errado com relação a espaçamento e disposição

matriz = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

matriz = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]


number_one = 1


# Errado
def retornofuncaoargs(
    arg_one, arg_two,
    arg_three, arg_four):
    # comentario de uma linha
    return (arg_one + arg_two)/(arg_three + arg_four)

# Certo
def retorno_funcao_args(arg_one, arg_two,
                        arg_three, arg_four):
    pass


# Certo
def retorno_funcao_args(arg_one,
                        arg_two,
                        arg_three,
                        arg_four):
    pass

def print_hi_with_message(name):
    pass


# wrong
def printhiwithname(x, y, z):
    t = (x+y)/z
    pass


# correto
def media_aluno(nota1, nota2, divisor):
    t = (nota1+nota2)/divisor
    pass


def funcao_ficticia(*args):
    pass


media_aluno(5,9,2)
media_aluno(7, 9, 2)
vetor = []

funcao_ficticia(vetor[1,2,3],{'key':2})
funcao_ficticia(vetor[1, 2, 3], {'key': 2})

if x==4: print (x,y); x,y=y,x

# Correta
if x == 4:
    print(x, y)
    x, y = y, x

# Mais sobre espaçamento
foo = (0,)  # Correto
bar=(0, )   # Errado


# wrong error
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
