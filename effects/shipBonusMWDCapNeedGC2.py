#Item: Deimos [Ship]
#Item: Thorax [Ship]
from customEffects import boostModListBySkillReq, increase
def shipBonusMWDCapNeedGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "capacitorCapacityMultiplier", "shipBonusGC2",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level, helper = increase)