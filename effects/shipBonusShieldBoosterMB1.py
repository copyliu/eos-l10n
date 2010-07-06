#Used by: Ship: Maelstrom
from customEffects import boostModListByReq
def shipBonusShieldBoosterMB1(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Battleship")
    boostModListByReq(fitting.modules, "shieldBonus", "shipBonusMB1",
                      lambda mod: mod.group.name == "Shield Booster",
                      self.item, extraMult = level)