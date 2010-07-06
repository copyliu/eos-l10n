#Used by: Ship: Blackbird
from customEffects import boostModListByReq
def caldariShipEwFalloffRangeCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "falloff", "shipBonusCC2",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)