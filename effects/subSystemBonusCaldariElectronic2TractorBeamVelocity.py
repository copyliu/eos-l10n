#Item: Tengu Electronics - Emergent Locus Analyzer [Subsystem]
from customEffects import boostModListByReq
def subSystemBonusCaldariElectronic2TractorBeamVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Electronic Systems")
    boostModListByReq(fitting.modules, "maxTractorVelocity", "subsystemBonusCaldariElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)