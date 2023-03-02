import json

def infoRevenue(revenue):
    smallestRev = float("inf")
    biggestRev = 0
    daysBiggerThanAvg = 0
    revenueSum = 0
    usefulDays = 0

    for item in revenue:
        # Armazenar o faturamento total e dias úteis de faturamento para o cálculo da média mensal.
        if (item["valor"] != 0.0):
            revenueSum += item["valor"]
            usefulDays += 1
            # Armazenar dia de menor faturamento e dia de maior faturamento.
            if (item["valor"] < smallestRev):
                smallestRev = item["valor"]
            elif (item["valor"] > biggestRev):
                biggestRev = item["valor"]
    
    # Cálculo da média considerando apenas dias úteis
    revenueAvg = revenueSum/usefulDays
    # Armazenar a quantidade de dias de faturamento maior que a média mensal
    for item in revenue:
        if (item["valor"] > revenueAvg):
            daysBiggerThanAvg += 1
    
    return smallestRev, biggestRev, daysBiggerThanAvg
        

def main():
    with open("dados/dados.json") as f:
        data = json.load(f)
    smallestRev, biggestRev, daysBiggerThanAvg = infoRevenue(data)
    print("Menor Faturamento Diário: " + str(smallestRev))
    print("Maior Faturamento Diário: " + str(biggestRev))
    print("Dias de faturamento maiores que a média mensal: " + str(daysBiggerThanAvg))

if (__name__ == "__main__"):
    main()