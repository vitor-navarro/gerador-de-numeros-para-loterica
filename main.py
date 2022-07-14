from random import randint

def defineQuantidadeDeNumeros():
    quantidadeDeNumeros = input("Qual a quantidade de números, padrão = 6\n")

    if quantidadeDeNumeros != "":
        try:
            quantidadeDeNumeros = int(quantidadeDeNumeros)
        except ValueError:
            defineQuantidadeDeNumeros()
            print("digite apenas números")
    else:
        quantidadeDeNumeros = 6

    return quantidadeDeNumeros

def defineNumeroMinimo():
    numeroMinimo = input("Digite qual vai ser o menor número possivel, padrão = 1\n")

    if numeroMinimo != "":
        try:
            numeroMinimo = int(numeroMinimo)
        except ValueError:
            defineNumeroMinimo()
            print("digite apenas números")
    else:
        numeroMinimo = 1

    return numeroMinimo

def defineNumeroMaximo(numeroMinimo):
    numeroMaximo = input("Digite qual vai ser o maior número possivel, padrão = 31\n")

    if numeroMaximo != "":
        try:
            numeroMaximo = int(numeroMaximo)

            if numeroMaximo < numeroMinimo:
                print("O número Máximo não pode ser maior que o número mínimo")
                defineNumeroMaximo(numeroMinimo)
        except ValueError:
            defineNumeroMaximo(numeroMinimo)
            print("digite apenas números")
    else:
        numeroMaximo = 31

    return numeroMaximo

def gerarNumeros(quantidadeDeNumeros,numeroMinimo, numeroMaximo):

    resultado = []
    while len(resultado) != quantidadeDeNumeros:
        r = randint(numeroMinimo, numeroMaximo)
        if r not in resultado:
            resultado.append(r)
    print(resultado)
    #for i in range((quantidadeDeNumeros)):
        #print(resultado[i])


if __name__ == '__main__':
    quantidadeDeNumeros = defineQuantidadeDeNumeros()
    numeroMinimo = defineNumeroMinimo()
    numeroMaximo = defineNumeroMaximo(numeroMinimo)

    gerarNumeros(quantidadeDeNumeros,numeroMinimo, numeroMaximo)
