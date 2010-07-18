#Item: Republic Fleet Firetail [Ship]
#Item: Rifter [Ship]
#Item: Slasher [Ship]
#Item: Stiletto [Ship]
from customEffects import boostModListBySkillReq
def shipProjectileTrackingMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusMF2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
