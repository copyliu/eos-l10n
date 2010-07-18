#Item: Bantam [Ship]
from customEffects import boostModListByReq
def shipMiningBonusCF(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonusCF2",
                      lambda mod: mod.group.name == "Mining Laser",
                      self.item, extraMult = level)