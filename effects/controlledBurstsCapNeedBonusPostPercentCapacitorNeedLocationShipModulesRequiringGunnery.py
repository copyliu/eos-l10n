#Item: Controlled Bursts [Skill]
#Item: Hardwiring - Inherent Implants 'Lancer' G0-Beta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Beta [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Beta [Implant]
from customEffects import boostModListBySkillReq
def controlledBurstsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringGunnery(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Gunnery",
                           self.item, extraMult = level)