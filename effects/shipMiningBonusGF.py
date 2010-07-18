#Item: Navitas
from customEffects import boostModListByReq
def shipMiningBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonusGF",
                      lambda mod: mod.group.name == "Mining Laser",
                      self.item, extraMult = level)