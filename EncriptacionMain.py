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


def reiniciar_diccionario(dic_alfabeto):
    lista = [' ',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             '.', ',', "'", '"', ':', ';', '!', '?']

    for i in lista:
        leer_diccionario(i, dic_alfabeto, ordenar=False)


def comprobar_diccionario_inverso(dic_alf, dic_inv):
    """
    Comprueba que todos los valores posibles del diccionario de alfabeto esté en el diccionario inverso. Si no está, o
    tiene un error, genera un diccionario inverso nuevo

    :param dic_alf:
    :param dic_inv:
    :return:
    """
    hay_que_hacer_cambios = False
    for key in dic_alf:
        valor = dic_alf[key]
        if str(valor) not in dic_inv or dic_inv[str(valor)] != key:
            hay_que_hacer_cambios = True
            break

    if hay_que_hacer_cambios:
        print('Faltan valores. Se vuelve a generar el inverso')
        return True
    else:
        print('Estan todos.')
        return False


def texto2numeros(string, dic_alfabeto):
    salidanumeros = ''

    for letra in range(len(string)):
        if string[letra] in dic_alfabeto:
            salidanumeros = salidanumeros + '{0:03d} '.format(dic_alfabeto[string[letra]])
        else:
            salidanumeros = salidanumeros + string[letra] + ' '

    return salidanumeros


def numeros2texto(string, dic_inverso):
    string = [str(int(i)) for i in string.split()]
    salidatexto = ''
    for numero in range(len(string)):
        if string[numero] in dic_inverso:
            salidatexto = salidatexto + dic_inverso[str(string[numero])]
        else:
            salidatexto = salidatexto + str(string[numero])

    return salidatexto


def comprobar_que_son_iguales(texto_nuevo, texto_control, verbose=False):
    contador = 0
    for n in range(len(texto_control.rstrip())):
        if texto_nuevo[n] == texto_control[n]:
            contador += 1

    if len(texto_control.rstrip()) == contador:
        if verbose:
            print('Coinciden')
        return True
    else:
        if verbose:
            print('No Coinciden')
        return False


def comprobar_mult(texto_new, texto_original, verbose=False):
    contador_mult = 0
    for i in range(len(texto_original)):
        comprobacion = comprobar_que_son_iguales(texto_new[i], texto_original[i])
        if comprobacion:
            contador_mult += 1
        else:
            raise ValueError('No son iguales')
    if contador_mult == len(texto_original):
        if verbose:
            print('coinciden')
        return True


def multiples_lineas(texto, diccionario, codificamos=True):
    longitud = len(texto)
    lista_final = []
    if codificamos:
        for i in range(longitud):
            transformado = texto2numeros(texto[i].rstrip(), dic_alfabeto=diccionario)
            lista_final.append(transformado.strip())
    else:
        for i in range(longitud):
            transformado = numeros2texto(texto[i].rstrip(), dic_inverso=diccionario)
            lista_final.append(transformado.strip())

    return lista_final


def main():

    dic_alfabeto = cargar_json()
    # Reinicio manual del diccionario
    if False:
        reiniciar_diccionario(dic_alfabeto)

    dic_inverso = cargar_json('Dic_alf_inv.json')

    # Comprobamos que se puede deshacer el cambio
    hay_que_corregir_inverso = comprobar_diccionario_inverso(dic_alfabeto, dic_inverso)
    if hay_que_corregir_inverso:
        generar_diccionario_inverso(dic_alfabeto)
        dic_inverso = cargar_json('Dic_alf_inv.json')

    f = open('base.txt', "r")
    lines_largo = list(f)

    print(lines_largo)
    print(lines_largo[0].rstrip())

    salida_multiples_numeros = multiples_lineas(lines_largo, dic_alfabeto)
    print(salida_multiples_numeros)

    salida_multiples_texto = multiples_lineas(salida_multiples_numeros, dic_inverso, codificamos=False)
    print(salida_multiples_texto)

    test_dum = comprobar_mult(salida_multiples_texto, lines_largo)
    print(test_dum)

    # ToDo: que funcione para varias lineas de texto (debería ser sencillo con funciones anidadas)
    # ToDO: guardar salida (dum2) a un fichero.txt y que tenga la opción de mostrar por pantalla
    # ToDo: encontrar el hueco donde se cifra.







if __name__ == "__main__":

    main()
