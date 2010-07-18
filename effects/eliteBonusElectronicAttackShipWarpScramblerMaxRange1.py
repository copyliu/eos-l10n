#Item: Keres
from customEffects import boostModListByReq
def eliteBonusElectronicAttackShipWarpScramblerMaxRange1(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusElectronicAttackShip1",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)