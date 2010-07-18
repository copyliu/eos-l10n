#Item: Golem [Ship]
#Item: Vargur [Ship]
from customEffects import boostModListByReq
def eliteBonusViolatorsShieldBonus2(self, fitting):
    skill, level = fitting.getCharSkill("Marauders")
    boostModListByReq(fitting.modules, "shieldBonus", "eliteBonusViolators2",
                      lambda mod: mod.group.name == "Shield Booster",
                      self.item, extraMult = level)