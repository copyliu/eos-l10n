#Used by: Item: Tengu Defensive - Amplification Node
from customEffects import boostModListByReq
def subsystemBonusCaldariDefensiveShieldBoostAmount(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Defensive Systems")
    boostModListByReq(fitting.modules, "shieldBonus", "subsystemBonusCaldariDefensive",
                      lambda mod: mod.group.name == "Shield Booster",
                      self.item, extraMult = level)