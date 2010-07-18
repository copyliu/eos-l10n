#Item: Scorpion [Ship]
from customEffects import boostModListByReq
def caldariShipEwFalloffRangeCB3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostModListByReq(fitting.modules, "falloff", "shipBonusCB3",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)