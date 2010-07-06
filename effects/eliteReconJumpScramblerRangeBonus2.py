#Used by: Ship: Arazu
#               Lachesis
from customEffects import boostModListByReq
def eliteReconJumpScramblerRangeBonus2(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusReconShip2",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)