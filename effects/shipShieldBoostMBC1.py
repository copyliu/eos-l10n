#Variations of item: Cyclone (3 of 3)
from customEffects import boostModListByReq
def shipShieldBoostMBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostModListByReq(fitting.modules, "shieldBonus", "shipBonusBC1",
                      lambda mod: mod.group.name == "Shield Booster",
                      self.item, extraMult = level)