#Item: Merlin
#Item: Raptor
from customEffects import boostModListBySkillReq
def shipHybridRangeBonusCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusCF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
