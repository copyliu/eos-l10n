#Item: Machariel [Ship]
from customEffects import boostModListBySkillReq
def shipPTurretFalloffBonusGB(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusGB",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item, extraMult = level)