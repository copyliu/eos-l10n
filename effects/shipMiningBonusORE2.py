#Items from group: Exhumer (3 of 3)
#Items from group: Mining Barge (3 of 3)
from customEffects import boostModListByReq
def shipMiningBonusORE2(self, fitting):
    skill, level = fitting.getCharSkill("Mining Barge")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonusORE2",
                      lambda mod: mod.group.name in ("Strip Miner", "Frequency Mining Laser"),
                      self.item, extraMult = level)
