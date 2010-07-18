#Item: Rook
from customEffects import boostModListByReq
def shipBonusHeavyLauncherRateOfFireCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostModListByReq(fitting.modules, "speed", "shipBonusCC2",
                      lambda mod: mod.group.name == "Missile Launcher Heavy",
                      self.item, extraMult = level)