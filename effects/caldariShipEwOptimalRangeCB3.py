#Item: Scorpion [Ship]
from customEffects import boostModListByReq
def caldariShipEwOptimalRangeCB3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusCB3",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)