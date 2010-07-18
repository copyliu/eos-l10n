#Variations of item: Large Inverted Signal Field Projector I (2 of 2) [Module]
#Variations of item: Medium Inverted Signal Field Projector I (2 of 2) [Module]
#Variations of item: Small Inverted Signal Field Projector I (2 of 2) [Module]
#Item: Signal Suppression [Skill]
from customEffects import boostModListByReq
def ewSkillSignalSuppressionScanResolutionBonus(self, fitting, level = 1, state = None):
    boostModListByReq(fitting.modules, "scanResolutionBonus", "scanSkillEwStrengthBonus",
                      lambda mod: mod.group.name == "Remote Sensor Damper",
                      self.item, extraMult = level)