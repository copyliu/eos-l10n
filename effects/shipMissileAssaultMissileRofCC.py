#Item: Osprey Navy Issue [Ship]
from customEffects import boostModListByReq
def shipMissileAssaultMissileRofCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "speed", "shipBonusCC",
                      lambda mod: mod.group.name == "Missile Launcher Assault",
                      self.item, extraMult = level)