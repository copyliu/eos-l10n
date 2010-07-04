#Used by: Ship: Vindicator
from customEffects import boostModListByReq
def shipBonusStasisWebSpeedFactorMB(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListByReq(fitting.modules, "speedFactor", "shipBonusMB",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)