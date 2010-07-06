#Used by: Scorpion
from customEffects import boostModListByReq
def caldariShipECMBurstOptimalRangeCB3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "ecmBurstRange", "shipBonusCB3",
                      lambda mod: mod.group.name == "ECM Burst",
                      self.item, extraMult = level)