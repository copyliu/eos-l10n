#Item: Blackbird [Ship]
from customEffects import boostModListByReq
def caldariShipEwOptimalRangeCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "maxRange", "shipBonusCC2",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)