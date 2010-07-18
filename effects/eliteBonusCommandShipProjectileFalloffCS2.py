#Item: Sleipnir [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipProjectileFalloffCS2(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "falloff", "eliteBonusCommandShips2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)