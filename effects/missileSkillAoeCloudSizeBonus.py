#Variations of item: Large Warhead Rigor Catalyst I (2 of 2)
#Variations of item: Medium Warhead Rigor Catalyst I (2 of 2)
#Variations of item: Small Warhead Rigor Catalyst I (2 of 2)
#Item: Guided Missile Precision
#Item: Hardwiring - Zainou 'Deadeye' ZMA10
#Item: Hardwiring - Zainou 'Deadeye' ZMA100
#Item: Hardwiring - Zainou 'Deadeye' ZMA1000
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeCloudSizeBonus(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "aoeCloudSize", "aoeCloudSizeBonus",
                            lambda skill: skill.name == "Standard Missiles" or \
                            skill.name == "Heavy Missiles" or \
                            skill.name == "Cruise Missiles",
                            self.item, extraMult = level)