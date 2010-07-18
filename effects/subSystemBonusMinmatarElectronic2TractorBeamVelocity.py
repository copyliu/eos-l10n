#Item: Loki Electronics - Emergent Locus Analyzer
from customEffects import boostModListByReq
def subSystemBonusMinmatarElectronic2TractorBeamVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boostModListByReq(fitting.modules, "maxTractorVelocity", "subsystemBonusMinmatarElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)