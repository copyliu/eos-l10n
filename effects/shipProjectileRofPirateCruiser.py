#Item: Cynabal [Ship]
from customEffects import boostModListBySkillReq
def shipProjectileRofPirateCruiser(self, fitting):
     boostModListBySkillReq(fitting.modules, "speed", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item)