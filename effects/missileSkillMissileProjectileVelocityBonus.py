#Variations of item: Large Hydraulic Bay Thrusters I (2 of 2) [Module]
#Variations of item: Medium Hydraulic Bay Thrusters I (2 of 2) [Module]
#Variations of item: Small Hydraulic Bay Thrusters I (2 of 2) [Module]
#Item: Hardwiring - Zainou 'Deadeye' ZML10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZML100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZML1000 [Implant]
#Item: Missile Projection [Skill]
from customEffects import boostAmmoListBySkillReq
def missileSkillMissileProjectileVelocityBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill":
        penalized = False
    else:
        penalized = True
        
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "speedFactor",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, useStackingPenalty = penalized, extraMult = level)
