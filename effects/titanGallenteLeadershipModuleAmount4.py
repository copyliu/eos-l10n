#Item: Erebus
from customEffects import boostModListByReq, increase
def titanGallenteLeadershipModuleAmount4(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Titan")
    boostModListByReq(fitting.modules, "maxGroupActive", "titanGallenteBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
