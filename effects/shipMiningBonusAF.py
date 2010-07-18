#Item: Tormentor [Ship]
from customEffects import boostModListByReq
def shipMiningBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonus2AF",
                      lambda mod: mod.group.name == "Mining Laser",
                      self.item, extraMult = level)