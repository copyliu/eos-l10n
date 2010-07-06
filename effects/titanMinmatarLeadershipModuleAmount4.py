#Used by: Ship: Ragnarok
from customEffects import boostModListByReq, increase
def titanMinmatarLeadershipModuleAmount4(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Titan")
    boostModListByReq(fitting.modules, "maxGroupActive", "titanMinmatarBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
