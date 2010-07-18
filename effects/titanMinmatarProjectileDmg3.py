#Item: Ragnarok [Ship]
from customEffects import boostModListBySkillReq
def titanMinmatarProjectileDmg3(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Titan")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "titanMinmatarBonus3",
                           lambda skill: skill.name == "Capital Projectile Turret",
                           self.item, extraMult = level)