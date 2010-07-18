#Item: Nyx
from customEffects import boostModListByReq, increase
def carrierGallenteLeadershipMaxGroupActive4(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    boostModListByReq(fitting.modules, "maxGroupActive", "carrierGallenteBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
