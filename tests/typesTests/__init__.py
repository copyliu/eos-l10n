import math
def getStackingPenaltyFactor(x = 2):
    return math.exp(-math.pow(x-1, 2) / 7.1289)
