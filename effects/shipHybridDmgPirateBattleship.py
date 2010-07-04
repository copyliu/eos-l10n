#Used by: Ship: Vindicator
from customEffects import boostModListBySkillReq
def shipHybridDmgPirateBattleship(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusPirateFaction",
                           lambda skill: skill.name == "Large Hybrid Turret",
                           self.item)