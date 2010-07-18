#Variations of item: Large Warhead Flare Catalyst I (2 of 2) [Module]
#Variations of item: Medium Warhead Flare Catalyst I (2 of 2) [Module]
#Variations of item: Small Warhead Flare Catalyst I (2 of 2) [Module]
#Item: Hardwiring - Zainou 'Deadeye' ZMS10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMS100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMS1000 [Implant]
#Item: Target Navigation Prediction [Skill]
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeVelocityBonus(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "aoeVelocityBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)