#Used by: Skill: Controlled Bursts
from customEffects import boostModListBySkillReq
def controlledBurstsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)