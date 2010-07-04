#Used by: Ship: Paladin
from customEffects import boostModListByReq
def shipBonusStasisWebSpeedFactorAB(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Battleship")
    boostModListByReq(fitting.modules, "speedFactor", "shipBonusAB",
                      lambda mod: mod.group.name == "Stasis Web",
                      self.item, extraMult = level)