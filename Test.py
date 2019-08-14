import numpy as np
import pandas as pd
import json
from Salida_limpia import mostrarresultados, stdrobusta
import IMGPlot as ImP
import matplotlib.pyplot as plt


def leer_diccionario(nombre, diccionario_, filename='Dic_alfabeto.json', ordenar=True):
    """
    Busca en el diccionario el valor dado. Si no existe, crea uno nuevo

    :param nombre:
    :param diccionario_:
    :param filename:
    :param ordenar:
    :return:
    """
    if nombre in diccionario_:
        return diccionario_[nombre]
    else:
        len_dic = len(diccionario_)
        diccionario_[nombre] = len_dic
        print('Nueva entrada en el diccionario: Letra {0} - Valor {1:03d}'.format(nombre, diccionario_[nombre]))
        guardar_json(diccionario_, filename, ordenar=ordenar)
        return diccionario_[nombre]


def mostrar_diccionario(nombre_diccionario):
    print("Mostramos el diccionario: ")
    for x, y in nombre_diccionario.items():
        print(x, y)


def guardar_json(variable, filename, ordenar=True):
    json_f = json.dumps(variable, indent=2, sort_keys=ordenar)
    f = open(filename, "w")
    f.write(json_f)
    f.close()


def cargar_json(filename='Dic_alfabeto.json'):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def generar_diccionario_inverso(dic, filename='Dic_alf_inv.json', ordenar=True):
    nuevo_diccionario = {}
    for key in dic:
        nuevo_diccionario[dic[key]] = key
    guardar_json(nuevo_diccionario, filename, ordenar=ordenar)


def reiniciar_diccionario():
    lista = [' ',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             '.', ',', "'", '"', ':', ';', '!', '?']

    for i in lista:
        leer_diccionario(i, dic_alfabeto, ordenar=False)


def comprobar_diccionario_inverso(dic_alf, dic_inv):
    for key in dic_alf:
        valor = dic_alf[key]
        if str(valor) not in dic_inv:
            print('Faltan valores. Se vuelve a generar el inverso')
            generar_diccionario_inverso(dic_alf)
            break
    print('Estan todos.')


dic_alfabeto = cargar_json()
dic_inverso = cargar_json('Dic_alf_inv.json')
comprobar_diccionario_inverso(dic_alfabeto, dic_inverso)

# True: reinicia el diccionario
if False:
    reiniciar_diccionario()


f = open('base.txt', "r")
lines = list(f)
# print(len(lines))
# print(lines)
# print(lines[0])

f = open('base2.txt', "r")
lines = list(f)
# print(len(lines))
# print(lines)
# print(lines[0])


def texto2numeros(string):
    salidanumeros = ''
    for letra in range(len(string)):
        if string[letra] in dic_alfabeto:
            salidanumeros = salidanumeros + '{0:03d} '.format(dic_alfabeto[string[letra]])
        else:
            salidanumeros = salidanumeros + string[letra] + ' '

    return salidanumeros


# def numeros2texto(string):
#     salidatexto = ''
#     for numero in range(len(string)):
#         if string[numero]



dum = texto2numeros(lines[0])

print(dum)











# mostrar_diccionario(dic_alfabeto)
