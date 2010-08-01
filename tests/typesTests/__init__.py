import math
#Pass 0 for 1st unpenalized module
def getStackingPenaltyFactor(x = 1):
    return math.exp(-math.pow(x, 2) / 7.1289)

def calculateBoostMultiplier(boostList, stackingPenalized):

    def calculateMultiplier(boostList, stackingPenalized):
        multiplier = 1
        for boostIndex in range(len(boostList)):
            if stackingPenalized: boost = (boostList[boostIndex]/100)*getStackingPenaltyFactor(boostIndex)
            else: boost = boostList[boostIndex]/100
            multiplier *= 1 + boost
        return multiplier

    boostListPositive = []
    boostListNegative = []
    for boostValue in boostList:
        if boostValue >= 0: boostListPositive.append(boostValue)
        else: boostListNegative.append(boostValue)
    boostListPositive = sorted(boostListPositive, reverse = True)
    boostListNegative = sorted(boostListNegative, reverse = False)
    multiplier = 1 * calculateMultiplier(boostListPositive, stackingPenalized) * calculateMultiplier(boostListNegative, stackingPenalized)
    return multiplier

def calculateMultiplierMultiplier(multiplierList, stackingPenalized):

    def calculateMultiplier(multiplierList, stackingPenalized):
        multiplier = 1
        for multiplierIndex in range(len(multiplierList)):
            if stackingPenalized: boost = (multiplierList[multiplierIndex] - 1)*getStackingPenaltyFactor(multiplierIndex)
            else: boost = multiplierList[multiplierIndex] - 1
            multiplier *= 1 + boost
        return multiplier

    multiplierListPositive = []
    multiplierListNegative = []
    for multiplierValue in multiplierList:
        if multiplierValue >= 1: multiplierListPositive.append(multiplierValue)
        elif multiplierValue >= 0: multiplierListNegative.append(multiplierValue)
    multiplierListPositive = sorted(multiplierListPositive, reverse = True)
    multiplierListNegative = sorted(multiplierListNegative, reverse = False)
    multiplier = 1 * calculateMultiplier(multiplierListPositive, stackingPenalized) * calculateMultiplier(multiplierListNegative, stackingPenalized)
    return multiplier
