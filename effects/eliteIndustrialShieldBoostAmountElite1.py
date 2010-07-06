#Used by: Ship: Prowler
#               Mastodon
#               Bustard
#               Crane
from customEffects import boostModListByReq
def eliteIndustrialShieldBoostAmountElite1(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boostModListByReq(fitting.modules, "shieldBonus", "eliteBonusIndustrial1",
                      lambda mod: mod.group.name == "Shield Booster", self.item,
                      extraMult = level)