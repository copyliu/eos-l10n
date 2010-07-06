#Used by: Ship: Utu
from customEffects import boostModListBySkillReq
def shipBonusSmallHybridTrackingSpeedATF2(self, fitting):
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusATF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item)