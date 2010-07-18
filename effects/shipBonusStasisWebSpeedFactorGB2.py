#Item: Kronos
from customEffects import boostModListByReq
def shipBonusStasisWebSpeedFactorGB2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Battleship")
    boostModListByReq(fitting.modules, "speedFactor", "shipBonusGB2",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)