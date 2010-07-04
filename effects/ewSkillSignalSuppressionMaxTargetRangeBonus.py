#Used by: Skill: Signal Suppression
from customEffects import boostModListByReq
def ewSkillSignalSuppressionMaxTargetRangeBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "maxTargetRangeBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)