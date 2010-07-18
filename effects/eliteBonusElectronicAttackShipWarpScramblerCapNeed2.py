#Item: Keres [Ship]
from customEffects import boostModListByReq
def eliteBonusElectronicAttackShipWarpScramblerCapNeed2(self, fitting):
    skill, level = fitting.getCharSkill("Electronic Attack Ships")
    boostModListByReq(fitting.modules, "capacitorNeed", "eliteBonusElectronicAttackShip2",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)