#Items from group: Transport Ship (4 of 8) [Ship]
from customEffects import boostModListByReq
def eliteIndustrialShieldBoostAmountElite1(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boostModListByReq(fitting.modules, "shieldBonus", "eliteBonusIndustrial1",
                      lambda mod: mod.group.name == "Shield Booster", self.item,
                      extraMult = level)