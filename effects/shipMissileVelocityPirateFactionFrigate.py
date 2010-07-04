#Used by: Ship: Worm
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityPirateFactionFrigate(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusPirateFaction",
                       lambda skill: skill.name == "Standard Missiles" or \
                       skill.name == "Rockets", self.item)