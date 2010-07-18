#Item: Rattlesnake
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityPirateFactionCruise(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusPirateFaction",
                            lambda skill: skill.name == "Cruise Missiles", self.item)