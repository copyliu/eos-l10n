#Variations of item: Tempest (3 of 4) [Ship]
#Item: Machariel [Ship]
#Item: Panther [Ship]
from customEffects import boostModListBySkillReq
def shipPTDmgBonusMB(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMB",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)
