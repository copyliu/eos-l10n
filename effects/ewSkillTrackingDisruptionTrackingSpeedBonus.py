#Variations of item: Large Tracking Diagnostic Subroutines I (2 of 2)
#Variations of item: Medium Tracking Diagnostic Subroutines I (2 of 2)
#Variations of item: Small Tracking Diagnostic Subroutines I (2 of 2)
#Item: Turret Destabilization
from customEffects import boostModListByReq
def ewSkillTrackingDisruptionTrackingSpeedBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)