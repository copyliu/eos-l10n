#Item: Cruor [Ship]
#Item: Succubus [Ship]
from customEffects import boostModListBySkillReq
def shipBonusSmallEnergyTurretDamagePirateFaction(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Small Energy Turret", self.item)