#Item: Dramiel [Ship]
from customEffects import boostModListBySkillReq
def shipProjectileTrackingGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusGF",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)