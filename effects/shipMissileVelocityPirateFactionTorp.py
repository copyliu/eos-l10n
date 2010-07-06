#Used by: Ship: Rattlesnake
from customEffects import boostAmmoListBySkillReq
def shipMissileVelocityPirateFactionTorp(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusPirateFaction",
                            lambda skill: skill.name == "Torpedoes", self.item)