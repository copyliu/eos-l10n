#Used by: Ship: Onyx
#               Broadsword
#               Devoter
#               Phobos
from customEffects import boostModListByReq
def eliteBonusHeavyInterdictorsWarpDisruptFieldGeneratorWarpScrambleRange2(self, fitting):
    skill, level = fitting.getCharSkill("Heavy Interdictors")
    boostModListByReq(fitting.modules, "warpScrambleRange", "eliteBonusHeavyInterdictors2",
                      lambda mod: mod.group.name == "Warp Disrupt Field Generator",
                      self.item, extraMult = level)