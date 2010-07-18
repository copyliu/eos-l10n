#Item: Machariel
from customEffects import boostModListBySkillReq
def shipProjectileRofPirateBattleship(self, fitting):
     boostModListBySkillReq(fitting.modules, "speed", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Large Projectile Turret",
                           self.item)