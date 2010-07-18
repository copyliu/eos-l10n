#Item: Bhaalgorn [Ship]
#Item: Nightmare [Ship]
from customEffects import boostModListBySkillReq
def shipLaserDamagePirateBattleship(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item)