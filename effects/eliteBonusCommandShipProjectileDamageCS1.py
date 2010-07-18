#Item: Sleipnir [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipProjectileDamageCS1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusCommandShips1",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)