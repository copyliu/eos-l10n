#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 7 > Armor Implants (3 of 3)
#Variations of item: Large Remote Repair Augmentor I (2 of 2) [Module]
#Variations of item: Medium Remote Repair Augmentor I (2 of 2) [Module]
#Variations of item: Small Remote Repair Augmentor I (2 of 2) [Module]
#Item: Remote Armor Repair Systems [Skill]
from customEffects import boostModListBySkillReq
def remoteArmorSystemsCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringRemoteArmorSystems(self, fitting, state = None, level = 1):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Remote Armor Repair Systems",
                           self.item, extraMult = level)