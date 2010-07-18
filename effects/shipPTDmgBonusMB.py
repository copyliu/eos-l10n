#Item: Machariel [Ship]
#Item: Panther [Ship]
#Item: Tempest [Ship]
#Item: Tempest Fleet Issue [Ship]
#Item: Tempest Tribal Issue [Ship]
from customEffects import boostModListBySkillReq
def shipPTDmgBonusMB(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMB",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
