import numpy as np
import pandas as pd
import json
from Salida_limpia import mostrarresultados, stdrobusta
import IMGPlot as ImP
import matplotlib.pyplot as plt


def leer_diccionario(nombre, diccionario_, filename='Dic_alfabeto.json'):
    """
    Busca en el diccionario el valor dado. Si no existe, crea uno nuevo

    :param nombre:
    :param diccionario_:
    :param filename:
    :return:
    """
    if nombre in diccionario_:
        return diccionario_[nombre]
    else:
        len_dic = len(diccionario_)
        diccionario_[nombre] = len_dic
        print('Nueva entrada en el diccionario: Letra {0} - Valor {1:03d}'.format(nombre, diccionario_[nombre]))
        guardar_json(diccionario_, filename)
        return diccionario_[nombre]


def mostrar_diccionario(nombre_diccionario):
    print("Mostramos el diccionario: ")
    for x, y in nombre_diccionario.items():
        print(x, y)


def guardar_json(variable, filename):
    json_f = json.dumps(variable, indent=2, sort_keys=True)
    f = open(filename, "w")
    f.write(json_f)
    f.close()


def cargar_json(filename='Dic_alfabeto.json'):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


dic_alfabeto = cargar_json()

f = open('base.txt', "r")
lines = list(f)
print(len(lines))
print(lines)
print(lines[0])

f = open('base2.txt', "r")
lines = list(f)
print(len(lines))
print(lines)
print(lines[0])


def transformar_a_numeros(texto):
    asdfasdf






#
#
# lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# for i in lista:
#     leer_diccionario(i, dic_alfabeto)
#
# mostrar_diccionario(dic_alfabeto)
