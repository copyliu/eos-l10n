#Used by: Skill: Missile Projection
#         Item : Hydraulic Bay Thrusters
from customEffects import boostAmmoListBySkillReq
def missileSkillMissileProjectileVelocityBonus(self, fitting, state = None, level = 1):
    if self.item.group.category.name == "Skill":
        penalized = False
    else:
        penalized = True
        
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "speedFactor",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, useStackingPenalty = penalized, extraMult = level)
