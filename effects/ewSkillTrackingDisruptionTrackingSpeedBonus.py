#Used by: Skill: Turret Destabilization
from customEffects import boostModListByReq
def ewSkillTrackingDisruptionTrackingSpeedBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "trackingSpeedBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Tracking Disruptor",
                      self.item, extraMult = level)