#Item: Proteus Electronics - Emergent Locus Analyzer
from customEffects import boostModListByReq
def subSystemBonusGallenteElectronic2TractorBeamRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boostModListByReq(fitting.modules, "maxRange", "subsystemBonusGallenteElectronic2",
                      lambda mod: mod.group.name == "Tractor Beam",
                      self.item, extraMult = level)