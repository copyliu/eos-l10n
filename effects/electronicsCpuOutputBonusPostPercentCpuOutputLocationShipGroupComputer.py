#Used by: Skill: Electronics
#       Implant: Hardwiring - Zainou 'Gypsy' KMB series
from customEffects import boost
def electronicsCpuOutputBonusPostPercentCpuOutputLocationShipGroupComputer(self, fitting, level = 1):
    boost(fitting.ship, "cpuOutput", "cpuOutputBonus2", self.item, extraMult = level)
