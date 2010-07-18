#Item: Hulk
from customEffects import boostModListByReq
def eliteBonusBargeMiningYield(self, fitting):
    skill, level = fitting.getCharSkill("Exhumers")
    boostModListByReq(fitting.modules, "miningAmount", "eliteBonusBarge1",
                      lambda mod: mod.group.name in ("Strip Miner", "Frequency Mining Laser"),
                      self.item, extraMult = level)
