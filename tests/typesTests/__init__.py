import math
#Pass 0 for 1st unpenalized module
def getStackingPenaltyFactor(x = 1):
    return math.exp(-math.pow(x, 2) / 7.1289)
