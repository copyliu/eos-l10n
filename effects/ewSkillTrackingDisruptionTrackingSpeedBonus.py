#Variations of item: Large Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Variations of item: Medium Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Variations of item: Small Tracking Diagnostic Subroutines I (2 of 2) [Module]
#Item: Turret Destabilization [Skill]
from customEffects import boostModListByReq
def ewSkillTrackingDisruptionTrackingSpeedBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)