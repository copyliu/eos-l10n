#Variations of item: Bellicose (3 of 3) [Ship]
#Variations of item: Rupture (3 of 3) [Ship]
#Variations of item: Stabber (3 of 3) [Ship]
#Item: Scythe Fleet Issue [Ship]
from customEffects import boostModListBySkillReq
def shipPTurretSpeedBonusMC(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusMC",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
