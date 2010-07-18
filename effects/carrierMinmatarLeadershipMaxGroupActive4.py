#Item: Hel [Ship]
from customEffects import boostModListByReq, increase
def carrierMinmatarLeadershipMaxGroupActive4(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Carrier")
    boostModListByReq(fitting.modules, "maxGroupActive", "carrierMinmatarBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
