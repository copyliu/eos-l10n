#Used by: Ship: Phantasm
from customEffects import boostModListBySkillReq
def shipBonusMediumEnergyTurretDamagePirateFaction(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Medium Energy Turret", self.item)