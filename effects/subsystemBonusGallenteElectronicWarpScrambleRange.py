#Used by: Item: Proteus Electronics - Friction Extension Processor
from customEffects import boostModListByReq
def subsystemBonusGallenteElectronicWarpScrambleRange(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Electronic Systems")
    boostModListByReq(fitting.modules, "maxRange", "subsystemBonusGallenteElectronic",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)