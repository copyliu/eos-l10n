#Item: Cynabal [Ship]
from customEffects import boostModListBySkillReq
def shipPTurretFalloffBonusGC(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "falloff", "shipBonusGC",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)