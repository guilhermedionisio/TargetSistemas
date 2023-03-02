def percentCalc(revenue):
    total = 0

    # Armazena as chaves do dicionário para calcular o percentual para cada chave.
    percentRevenue = dict.fromkeys(revenue.keys())
    # Calcula a soma dos faturamentos para ser possível calcular o valor percentual por estado.
    for key in revenue.keys():
        total += revenue[key]
    
    # Calcula o percentual de cada estado dividindo o faturamento de cada estado pelo
    # faturamento total e armazena no dicionario baseado na sua chave.
    for key in percentRevenue.keys():
        percentRevenue[key] = round(revenue[key]/total * 100, 1)
    
    return percentRevenue


def main():
    revenue = {"SP":67836.43, "RJ":36678.66, "MG":29229.88, "ES":27165.48, "Outros":19849.53}
    percentRevenue = percentCalc(revenue)
    for key in percentRevenue.keys():
        print("Faturamento do Estado "+key+":"+str(percentRevenue[key]))

if (__name__ == "__main__"):
    main()