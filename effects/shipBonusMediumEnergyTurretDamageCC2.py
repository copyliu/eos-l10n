#Item: Phantasm
from customEffects import boostModListBySkillReq
def shipBonusMediumEnergyTurretDamageCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusCC2",
                           lambda skill: skill.name == "Medium Energy Turret",
                           self.item, extraMult = level)