#Used by: Ship: Utu
from customEffects import boostModListByReq
def shipBonusWarpScramblerMaxRangeGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusGF2",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)