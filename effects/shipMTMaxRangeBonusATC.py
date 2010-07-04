#Used by: Ship: Mimir
from customEffects import boostModListBySkillReq
def shipMTMaxRangeBonusATC(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "shipBonusATC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item)