#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Electronics Implants (3 of 6)
#Item: Electronics [Skill]
from customEffects import boost
def electronicsCpuOutputBonusPostPercentCpuOutputLocationShipGroupComputer(self, fitting, level = 1):
    boost(fitting.ship, "cpuOutput", "cpuOutputBonus2", self.item, extraMult = level)
