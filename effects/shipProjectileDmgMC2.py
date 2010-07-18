#Variations of item: Rupture (2 of 3) [Ship]
#Item: Cynabal [Ship]
from customEffects import boostModListBySkillReq
def shipProjectileDmgMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)