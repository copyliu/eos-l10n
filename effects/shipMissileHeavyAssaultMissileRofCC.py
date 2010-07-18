#Item: Osprey Navy Issue [Ship]
from customEffects import boostModListByReq
def shipMissileHeavyAssaultMissileRofCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "speed", "shipBonusCC",
                      lambda mod: mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)