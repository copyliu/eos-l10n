#Used by: Ship: Gila
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityPirateFactionHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusPirateFaction",
                       lambda skill: skill.name == "Heavy Missiles", self.item)