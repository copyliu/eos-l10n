#Used by: Ship: Gila
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityPirateFactionHeavyAssault(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusPirateFaction",
                       lambda skill: skill.name == "Heavy Assault Missiles", self.item)