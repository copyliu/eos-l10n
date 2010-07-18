#Item: Stabber Fleet Issue [Ship]
from customEffects import boostModListBySkillReq
def shipBonusProjectileTrackingMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusMC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
