#Variations of item: Prophecy (2 of 3) [Ship]
from customEffects import boostModListByReq
def shipLaserCapABC2(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusBC2",
                      lambda mod: mod.group.name == "Energy Weapon", self.item,
                      extraMult = level)