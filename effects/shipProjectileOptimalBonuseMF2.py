#Item: Cheetah [Ship]
from customEffects import boostModListBySkillReq
def shipProjectileOptimalBonuseMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusMF2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)