import numpy as np
import pandas as pd
from Salida_limpia import mostrarresultados, stdrobusta
import IMGPlot as ImP
import matplotlib.pyplot as plt
from EncriptacionMain import generar_diccionario_inverso, texto2numeros, numeros2texto, mostrar_diccionario


def codificar(texto, descifrado, clave, dic_inverso):
    if type(texto) == list:
        eslista = True
    else:
        eslista = False

    print(texto, eslista, descifrado, clave)

    dic_r_n = generar_dic_romano_numero(clave)
    dic_r_n_inv = generar_diccionario_inverso(dic_r_n, filename='Dic_romana.json', ordenar=False)
    print('######')

    # Cifrado
    entrada = [i for i in texto[0].split()]
    print(entrada)
    print('======')
    transformado_romano = convertir_diccionario(entrada, dic_r_n_inv, espacio='')
    print(transformado_romano)
    # ToDo: aquí se guardaría en un fichero .txt

    # Descifrar
    # Pasamos a números
    deshacer = convertir_diccionario(transformado_romano, dic_r_n)  # Esta entrada es una sola linea
    print(deshacer)

    # Pasamos a letras
    deshacer2 = convertir_diccionario(deshacer.split(), dic_inverso, espacio='')
    print(deshacer2)


def convertir_diccionario(lista, diccionario, espacio=' '):
    salida = ''
    # lista = [i for i in string.split()]
    print(lista)
    for letra in range(len(lista)):
        if lista[letra] in diccionario:
            salida = salida + '{0}{1}'.format(diccionario[str(lista[letra])], espacio)
        else:
            salida = salida + string[letra] + ' '

    return salida


def generar_dic_romano_numero(clave):
    dic_romana = {}
    for letra in clave:
        if letra not in dic_romana:
            len_dic = len(dic_romana)
            dic_romana[letra] = str(len_dic)

    lista_letras = [' ',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    '.', ',', "'", '"', ':', ';', '!', '?']

    for letra in lista_letras:
        if letra not in dic_romana:
            len_dic = len(dic_romana)
            dic_romana[letra] = str(len_dic)

    return dic_romana


def generar_dic_texto2texto(dic_romana, dic_inv):
    dic_t2t = {}

    for key in dic_romana:
        if key not in dic_t2t:
            dic_t2t[key] = dic_inv[str(dic_romana[key])]

    return dic_t2t

