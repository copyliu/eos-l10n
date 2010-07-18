#Items from group: Cyber Armor (3 of 24)
#Items from group: Rig Armor (6 of 54)
#Variations of item: Medium Remote Repair Augmentor I (2 of 2)
#Item: Remote Armor Repair Systems
from customEffects import boostModListBySkillReq
def remoteArmorSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringRemoteArmorSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Remote Armor Repair Systems",
                           self.item, extraMult = level)