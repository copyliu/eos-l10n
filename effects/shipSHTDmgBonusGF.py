#Variations of item: Atron (3 of 3) [Ship]
#Variations of item: Incursus (3 of 3) [Ship]
#Item: Federation Navy Comet [Ship]
#Item: Helios [Ship]
#Item: Maulus [Ship]
#Item: Tristan [Ship]
from customEffects import boostModListBySkillReq
def shipSHTDmgBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGF",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
