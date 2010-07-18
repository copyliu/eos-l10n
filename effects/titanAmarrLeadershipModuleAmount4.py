#Item: Avatar [Ship]
from customEffects import boostModListByReq, increase
def titanAmarrLeadershipModuleAmount4(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Titan")
    boostModListByReq(fitting.modules, "maxGroupActive", "titanAmarrBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
