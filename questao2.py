def fiboCheck(numToCheck):
    # Varíavel para checar a presença do número na sequência.
    isFibo = False
    # Variáveis para armazenar os 2 últimos números da sequência.
    firstNum = 0
    lastNum = 1

    # Calcula a sequência de Fibonacci até o número desejado.
    while (lastNum < numToCheck):
        aux = lastNum
        lastNum += firstNum
        firstNum = aux
    
    # Checa se o número desejado foi o ultimo número calculado na sequência.
    # Checa o caso específico do número desejado ser o 1o número da sequência.
    if (lastNum == numToCheck or numToCheck == 0):
        isFibo = True

    return isFibo


def main():
    # Variável que armazena o número desejado para a checagem.
    numToCheck = 1
    isFibo = fiboCheck(numToCheck)
    if (isFibo):
        print("O número escolhido pertence a sequência de Fibonacci.")
    else:
        print("O número escolhido não pertence a sequência de Fibonacci.")

if (__name__ == "__main__"):
    main()