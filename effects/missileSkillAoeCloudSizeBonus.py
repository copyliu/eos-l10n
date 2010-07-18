#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Missile Implants (3 of 6)
#Variations of item: Large Warhead Rigor Catalyst I (2 of 2) [Module]
#Variations of item: Medium Warhead Rigor Catalyst I (2 of 2) [Module]
#Variations of item: Small Warhead Rigor Catalyst I (2 of 2) [Module]
#Item: Guided Missile Precision [Skill]
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeCloudSizeBonus(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "Standard Missiles" or \
                            skill.name == "Heavy Missiles" or \
                            skill.name == "Cruise Missiles",
                            self.item, extraMult = level)