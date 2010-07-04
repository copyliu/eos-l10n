#Used by: Ship: Tempest
#               Tempest Fleet Issue
#               Tempest Tribal Issue
#               Machariel
#               Panther
from customEffects import boostModListBySkillReq
def shipPTDmgBonusMB(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMB",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
