#Item: Raptor
from customEffects import boostModListBySkillReq
def shipHybridDamageBonusCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusCF",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)