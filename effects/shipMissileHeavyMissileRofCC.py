#Item: Osprey Navy Issue
from customEffects import boostModListByReq
def shipMissileHeavyMissileRofCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "speed", "shipBonusCC",
                      lambda mod: mod.group.name == "Missile Launcher Heavy",
                      self.item, extraMult = level)