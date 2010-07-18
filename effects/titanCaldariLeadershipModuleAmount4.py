#Item: Leviathan
from customEffects import boostModListByReq, increase
def titanCaldariLeadershipModuleAmount4(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Titan")
    boostModListByReq(fitting.modules, "maxGroupActive", "titanCaldariBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
