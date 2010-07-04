#Used by: Ship: Griffin
#               Kitsune
from customEffects import boostModListByReq
def caldariShipEwCapacitorNeedCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusCF2",
                      lambda mod: mod.group.name == "ECM", self.item,
                      extraMult = level)