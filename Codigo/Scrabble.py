diccionario = {
    'A' : False,
    'B' : False,
    'C' : False,
    'D' : False,
    'E' : False,
    'F' : False,
    'G' : False,
    'H' : False,
    'I' : False,
    'J' : False,
    'K' : False,
    'L' : False,
    'M' : False,
    'N' : False,
    'O' : False,
    'P' : False,
    'Q' : False,
    'R' : False,
    'S' : False,
    'T' : False,
    'U' : False,
    'V' : False,
    'W' : False,
    'X' : False,
    'Y' : False,
    'Z' : False,
}


def verificarDuplicados (palabra):
    letrasDup = []

    for i in range (len(palabra) - 1):
        letra = palabra[i]
        letraSiguiente = palabra[i+1]

        if letra == letraSiguiente:
            diccionario[letra] = True
            
def buscarSecuencias ():
    archivo = open ('sowpods.txt', 'r')
    palabras = []
    for palabra in archivo:
        verificarDuplicados(palabra)

if __name__ == '__main__':
    buscarSecuencias()
    letrasNoRepetidas = []
    for clave in diccionario:
        if not diccionario[clave]:
            letrasNoRepetidas.append(clave)

    print letrasNoRepetidas
