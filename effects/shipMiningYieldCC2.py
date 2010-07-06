#Used by: Ship: Osprey
from customEffects import boostModListByReq
def shipMiningYieldCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "miningAmount", "shipBonusCC2",
                      lambda mod: mod.group.name == "Mining Laser",
                      self.item, extraMult = level)