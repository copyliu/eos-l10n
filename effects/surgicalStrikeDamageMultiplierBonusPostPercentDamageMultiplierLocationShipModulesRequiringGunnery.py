#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Gunnery Implants (3 of 9)
#Item: Cerebral Accelerator [Implant]
from customEffects import boostModListBySkillReq
def surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringGunnery(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Gunnery", self.item)