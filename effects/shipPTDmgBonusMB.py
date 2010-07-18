#Item: Machariel
#Item: Panther
#Item: Tempest
#Item: Tempest Fleet Issue
#Item: Tempest Tribal Issue
from customEffects import boostModListBySkillReq
def shipPTDmgBonusMB(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMB",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
