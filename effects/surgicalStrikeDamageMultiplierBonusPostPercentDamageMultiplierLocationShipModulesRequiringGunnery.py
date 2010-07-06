#Used by: Item: Eifyr & Co 'Gunslinger' CX-X
from customEffects import boostModListBySkillReq
def surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringGunnery(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Gunnery", self.item)