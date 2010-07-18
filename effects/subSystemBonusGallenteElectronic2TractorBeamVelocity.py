#Item: Proteus Electronics - Emergent Locus Analyzer [Subsystem]
from customEffects import boostModListByReq
def subSystemBonusGallenteElectronic2TractorBeamVelocity(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boostModListByReq(fitting.modules, "maxTractorVelocity", "subsystemBonusGallenteElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)