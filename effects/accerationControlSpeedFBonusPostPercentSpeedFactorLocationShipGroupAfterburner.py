#Used by: Item: Hardwiring - 'Rogue' MY-X
from customEffects import boostModListByReq
def accerationControlSpeedFBonusPostPercentSpeedFactorLocationShipGroupAfterburner(self, fitting):
    boostModListByReq(fitting.modules, "speedFactor", "speedFBonus",
                      lambda mod: mod.group.name == "Afterburner", self.item)