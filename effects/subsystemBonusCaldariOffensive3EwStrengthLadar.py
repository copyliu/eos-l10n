#Item: Tengu Offensive - Rifling Launcher Pattern
from customEffects import boostModListByReq
def subsystemBonusCaldariOffensive3EwStrengthLadar(self, fitting, state):
    skill, level = fitting.getCharSkill("Caldari Offensive Systems")
    boostModListByReq(fitting.modules, "scanLadarStrengthBonus",
                      "subsystemBonusCaldariOffensive3",
                      lambda mod: mod.group.name == "ECM",
                      self.item, extraMult = level)