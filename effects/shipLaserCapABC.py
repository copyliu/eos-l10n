#Item: Harbinger [Ship]
from customEffects import boostModListByReq
def shipLaserCapABC(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusBC1",
                      lambda mod: mod.group.name == "Energy Weapon", self.item,
                      extraMult = level)