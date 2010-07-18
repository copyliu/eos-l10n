#Item: Burst [Ship]
from customEffects import boostModListByReq
def shipMiningBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonusMF",
                      lambda mod: mod.group.name == "Mining Laser",
                      self.item, extraMult = level)