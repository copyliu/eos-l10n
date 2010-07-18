#Item: Cynabal [Ship]
#Item: Muninn [Ship]
#Item: Rupture [Ship]
from customEffects import boostModListBySkillReq
def shipProjectileDmgMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)