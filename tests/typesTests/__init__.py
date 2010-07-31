import math
#Pass 0 for 1st unpenalized module
def getStackingPenaltyFactor(x = 1):
    return math.exp(-math.pow(x, 2) / 7.1289)

def calculateBoostMultiplier(boostList, stackingPenalized):
    boostList = sorted(boostList, reverse = True)
    multiplier = 1
    for boostIndex in range(len(boostList)):
        if stackingPenalized: boost = (boostList[boostIndex]/100)*getStackingPenaltyFactor(boostIndex)
        else: boost = boostList[boostIndex]/100
        multiplier *= 1 + boost
    return multiplier
