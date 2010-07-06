#Used by: Skill: Remote Armor Repair Systems
#         Item : Remote Repair Augmentor
from customEffects import boostModListBySkillReq
def remoteArmorSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringRemoteArmorSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Remote Armor Repair Systems",
                           self.item, extraMult = level)