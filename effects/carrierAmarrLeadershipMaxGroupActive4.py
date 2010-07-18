#Item: Aeon [Ship]
from customEffects import boostModListByReq, increase
def carrierAmarrLeadershipMaxGroupActive4(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Carrier")
    boostModListByReq(fitting.modules, "maxGroupActive", "carrierAmarrBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
