#Item: Focused Warp Disruption [Charge]
from customEffects import boost
def scriptWarpScrambleRangeBonus(self, fitting, containerModule):
    boost(containerModule, "warpScrambleRange", "warpScrambleRangeBonus", self.item)