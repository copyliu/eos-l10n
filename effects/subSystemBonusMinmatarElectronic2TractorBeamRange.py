#Item: Loki Electronics - Emergent Locus Analyzer
from customEffects import boostModListByReq
def subSystemBonusMinmatarElectronic2TractorBeamRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Minmatar Electronic Systems")
    boostModListByReq(fitting.modules, "maxRange", "subsystemBonusMinmatarElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)