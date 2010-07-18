#Item: Hurricane [Ship]
from customEffects import boostModListBySkillReq
def shipBonusProjectileDamageBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusBC1",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)