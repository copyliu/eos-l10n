#Item: Legion Electronics - Emergent Locus Analyzer
from customEffects import boostModListByReq
def subSystemBonusAmarrElectronic2TractorBeamVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Electronic Systems")
    boostModListByReq(fitting.modules, "maxTractorVelocity", "subsystemBonusAmarrElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)