#Item: Gila
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityPirateFactionLight(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusPirateFaction",
                       lambda skill: skill.name == "Standard Missiles", self.item)