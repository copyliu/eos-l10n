#Used by: Ship: Succubus
from customEffects import boostModListBySkillReq
def shipBonusSmallEnergyTurretDamageCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusCF2",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)