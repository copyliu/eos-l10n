#Item: Flycatcher
from customEffects import boostAmmoListBySkillReq
def shipBonusStandardMissileAoeDamageReductionFactorDF2(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "aoeDamageReductionFactor", "shipBonusDF2",
                       lambda skill: skill.name == "Standard Missiles",
                       self.item, extraMult = level)