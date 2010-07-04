#Used by: Ship: Hyena
#               Daredevil
from customEffects import boostModListBySkillReq, increase
def shipBonusMWDCapNeedMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "capacitorCapacityMultiplier", "shipBonusMF",
                           lambda skill: skill.name == "High Speed Maneuvering",
                           self.item, extraMult = level, helper = increase)