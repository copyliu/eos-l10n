#Used by: Ammo: Focused Warp Disruption
from customEffects import boost
def scriptWarpScrambleRangeBonus(self, fitting, containerModule):
    boost(containerModule, "warpScrambleRange", "warpScrambleRangeBonus", self.item)