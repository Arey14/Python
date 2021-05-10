import random as rd
archivo = "/home/augusto/Escritorio/Python/Python-Intermedio/Archivos/data2.txt"

def run():
    palabra = selection(read())
    oculta = []
    faltantes = len(palabra)
    for i in range(0, len(palabra)):
        oculta.append("_")
    while faltantes != 0:
        print("Adivina la palabra!")
        print(*oculta)
        letra = input("Ingresa una letra: ")
        for i in range(0,len(palabra)):
            if palabra[i] == letra:
                oculta[i] = letra
                faltantes = faltantes -1
    else:
        print("Ganaste!! La palabra era ", *oculta)


def read():
    words = []
    with open(archivo, "r", encoding="latin1") as f:
        for line in f:
            words.append(line.replace("\n", ""))
    return words

def selection(x):
    palabra = []
    randomword = rd.choice(x)
    for i in randomword:
        palabra.append(i)
    return palabra

if __name__ == '__main__':
    run()