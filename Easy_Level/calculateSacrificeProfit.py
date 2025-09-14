from typing import List

def calculateSacrificeProfit(buyPrice: List[float], sellPrice: List[float]) -> float:
    return sum(sellPrice) - sum(buyPrice)
