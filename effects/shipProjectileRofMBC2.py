#Items from market group: Ships > Command Ships > Minmatar (2 of 2)
#Item: Cyclone
#Item: Hurricane
from customEffects import boostModListBySkillReq
def shipProjectileRofMBC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusBC2",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)