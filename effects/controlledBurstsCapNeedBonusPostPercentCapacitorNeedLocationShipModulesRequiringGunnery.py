#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Gunnery Implants (3 of 9)
#Item: Controlled Bursts
from customEffects import boostModListBySkillReq
def controlledBurstsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)