#Item: Legion Electronics - Emergent Locus Analyzer [Subsystem]
from customEffects import boostModListByReq
def subSystemBonusAmarrElectronic2TractorBeamRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boostModListByReq(fitting.modules, "maxRange", "subsystemBonusAmarrElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)