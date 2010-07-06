#Used by: Ship: Cyclone
#               Sleipnir
#               Claymore
#               Hurricane
from customEffects import boostModListBySkillReq
def shipProjectileRofMBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusBC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)