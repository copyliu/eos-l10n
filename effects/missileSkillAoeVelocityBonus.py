#Variations of item: Large Warhead Flare Catalyst I (2 of 2)
#Variations of item: Medium Warhead Flare Catalyst I (2 of 2)
#Variations of item: Small Warhead Flare Catalyst I (2 of 2)
#Item: Hardwiring - Zainou 'Deadeye' ZMS10
#Item: Hardwiring - Zainou 'Deadeye' ZMS100
#Item: Hardwiring - Zainou 'Deadeye' ZMS1000
#Item: Target Navigation Prediction
from customEffects import boostAmmoListBySkillReq
def missileSkillAoeVelocityBonus(self, fitting, level = 1, state = None):
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "aoeVelocityBonus",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)