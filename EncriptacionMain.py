import numpy as np
import pandas as pd
import json
from Salida_limpia import mostrarresultados, stdrobusta
import IMGPlot as ImP
import matplotlib.pyplot as plt
import Romana as Rom
import argparse


def generar_diccionario(nombre, diccionario_, filename='Dic_alfabeto.json', ordenar=True):
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
    if filename is not None:
        guardar_json(nuevo_diccionario, filename, ordenar=ordenar)
    return nuevo_diccionario


def reiniciar_diccionario(dic_alfabeto):
    dic_alfabeto = {}
    lista = [' ',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             '.', ',', "'", '"', ':', ';', '!', '?']

    for i in lista:
        generar_diccionario(i, dic_alfabeto, ordenar=False)


def comprobar_diccionario_inverso(dic_alf, dic_inv, verbose=False):
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
        if verbose:
            print('Faltan valores. Se vuelve a generar el inverso')
        return True
    else:
        if verbose:
            print('Estan todos.')
        return False


def texto2numeros(string, dic_alfabeto):
    salidanumeros = ''

    for letra in range(len(string)):
        if string[letra] in dic_alfabeto:
            salidanumeros = salidanumeros + '{0:d} '.format(dic_alfabeto[string[letra]])
        else:
            salidanumeros = salidanumeros + string[letra] + ' '

    return salidanumeros


def numeros2texto(string, dic_inverso):
    # Separa por espacios
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


def guardar_txt(lista, filename):
    with open(filename, 'w') as f:
        for item in lista:
            f.write("%s\n" % item)


def cargar_txt(filename):
    f = open(filename, "r")
    lines_largo = list(f)
    return lines_largo


def mostrar_por_pantalla(lista):
    for item in lista:
        print(item)


def limpiar_strip_listas(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].strip()
    return lista


def encrypt_information(entrada, cifr, save, dic_alfabeto, dic_inverso,
                        tipo_de_encriptacion='Romana', clave='Password'):
    print('Encrypt Information\n#########################################################')
    if tipo_de_encriptacion == 'Romana':
        print('Romana')
        if cifr:
            salida = Rom.codificar(entrada, clave=clave)
        else:
            salida = Rom.descodificar(entrada, clave=clave, dic_inverso=dic_inverso)

        if save is not None:
            guardar_txt(salida, save)
    else:
        salida = None
        # ToDo: El metodo romano que esté en un archivo aparte y que lo ejecute directamente desde allí en una función
        #  única que simplemente le metas la palabra clave y te devuelva el resultado cifrado.
    return salida


def argumentos_entrada(args, default_file, default_save, default_cifrar, default_password, default_tipo):
    # Aquí vienen las comprobaciones de que los argumentos de entrada sean correctos.
    if args.file == default_file:
        # Cambiar aquí para que meta el archivo en cuestión
        file = input("Introducir nombre del archivo que se quiere cifrar/descifrar:[" + default_file + "] ") \
               or default_file
    else:
        file = args.file

    if not args.skipsave:
        if args.save == default_save:
            save = input("Introducir nombre del archivo en el que se quiere guardar:[" + default_save + "] ") \
                   or default_save
        else:
            save = args.save
    else:
        save = None

    if not any([args.cifrar, args.descifrar]):
        if default_cifrar:
            ciframos = input("Ciframos?[Y]/N: ") or default_cifrar
        else:
            ciframos = input("Ciframos?Y/[N]: ") or default_cifrar

        if ciframos in ['Y', 'y', '1']:
            ciframos = True
        elif ciframos in ['N', 'n', '0']:
            ciframos = False
        else:
            raise ValueError('No es una entrada válida. Se busca Y/N, y/n, 1/0')
    else:
        if args.cifrar:
            ciframos = True
        else:
            ciframos = False

    if any([args.romana]):  # Aquí vienen más opciones de cifrado
        if args.clave == default_password:
            clave = input("Este metodo requiere de contraseñas:" + default_password + "] ") or default_password
        else:
            clave = args.password
    else:
        clave = None

    if any([args.romana]):
        if args.romana:
            tipo = 'Romana'
        else:
            tipo = default_tipo
    else:
        raise ValueError('No hay tipo')

    return tipo, file, save, ciframos, clave


def main():
    # ---------------Valores por defecto-------------------------------------------
    default_password = 'password'
    default_file = 'Cifrado.txt'
    default_cifrar = 'Y'
    default_save = 'Salida.txt'
    default_tipo = 'Romana'
    # -----------------------------------------------------------------------------

    parser = argparse.ArgumentParser(description="Encriptacion usando multiples metodos")
    group = parser.add_mutually_exclusive_group()

    grupo_cifrado = parser.add_mutually_exclusive_group()
    grupo_descifrar_cifrar = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("--reiniciar", action="store_true", help='Reinicar el diccionario del alfabeto')
    parser.add_argument('-p', '--password', default=default_password, type=str,
                        help='Password in case it needs a password')
    parser.add_argument('-ss', '--skipsave', action='store_true', help='Evita guardar el archivo final')
    parser.add_argument('-s', '--save', default=default_save, type=str, help='Donde guardar.')

    grupo_descifrar_cifrar.add_argument('-c', '--cifrar', action="store_true", help='Ciframos el archivo dado')
    grupo_descifrar_cifrar.add_argument('-d', '--descifrar', action="store_true", help='Desciframos el archivo dado')

    grupo_cifrado.add_argument('-rom', '--romana', action="store_true", help='Metodo Romano')
    # Aquí vendrán el resto de los métodos

    parser.add_argument('-f', '--file', default=default_file, type=str, help='sobre el que operar')

    args = parser.parse_args()

    tipo, file, save, ciframos, clave = argumentos_entrada(args, default_file, default_save, default_cifrar, default_password, default_tipo)

    dic_alfabeto = cargar_json()
    # Reinicio manual del diccionario
    if args.reiniciar:
        reiniciar_diccionario(dic_alfabeto)

    dic_inverso = cargar_json('Dic_alf_inv.json')

    # Comprobamos que se puede deshacer el cambio
    hay_que_corregir_inverso = comprobar_diccionario_inverso(dic_alfabeto, dic_inverso)
    if hay_que_corregir_inverso:
        dic_inverso = generar_diccionario_inverso(dic_alfabeto)
        # dic_inverso = cargar_json('Dic_alf_inv.json')

    lines_largo = cargar_txt(file)

    # cargado = limpiar_strip_listas(cargar_txt('Cifrado.txt'))  # ToDo: Mirar si esto sirve de algo

    entrada_multiple_numeros = multiples_lineas(lines_largo, dic_alfabeto)

    # Ahora que tenemos una serie de números, encriptamos la información
    # ToDo: encriptamos
    salida_encryption = encrypt_information(entrada_multiple_numeros, tipo_de_encriptacion=tipo, cifr=ciframos,
                                            save=save, dic_alfabeto=dic_alfabeto, dic_inverso=dic_inverso, clave=clave)

    salida_multiples_texto = multiples_lineas(salida_encryption, dic_inverso, codificamos=False)
    # print(salida_multiples_texto)

    test_dum = comprobar_mult(salida_multiples_texto, lines_largo)
    # print(test_dum)

    guardar_txt(entrada_multiple_numeros, 'archivo_numeros.txt')
    guardar_txt(salida_multiples_texto, 'archivo_texto.txt')







if __name__ == "__main__":

    main()
