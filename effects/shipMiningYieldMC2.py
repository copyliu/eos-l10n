#Item: Scythe [Ship]
from customEffects import boostModListByReq
def shipMiningYieldMC2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonusMC2",
                      lambda mod: mod.group.name == "Mining Laser",
                      self.item, extraMult = level)