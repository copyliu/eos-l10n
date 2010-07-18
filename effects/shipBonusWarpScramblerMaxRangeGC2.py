from customEffects import boostModListByReq
def shipBonusWarpScramblerMaxRangeGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusGC2",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)