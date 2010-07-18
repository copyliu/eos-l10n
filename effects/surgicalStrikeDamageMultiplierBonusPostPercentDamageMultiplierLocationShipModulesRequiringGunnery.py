#Item: Cerebral Accelerator [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' CX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' CX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' CX-2 [Implant]
from customEffects import boostModListBySkillReq
def surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringGunnery(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Gunnery", self.item)