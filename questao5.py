def reverseString(originalString):
    reversedString = ""

    # Loop "for" que percorre a string original de trás pra frente e
    # acrescenta à varáivel que armazena a string revertida.
    for idx in range(len(originalString) - 1, -1, -1):
        reversedString += originalString[idx]
    
    return reversedString


def main():
    originalString = "Frase Exemplo!."
    reversedString = reverseString(originalString)
    print(reversedString)

if (__name__ == "__main__"):
    main()