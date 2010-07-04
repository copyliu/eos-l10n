#Used by: Ship: Rook
#               Falcon
from customEffects import boostModListByReq
def caldariShipEwCapacitorNeedCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusCC",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)