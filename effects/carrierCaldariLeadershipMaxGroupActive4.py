#Used by: Ship: Wyvern
from customEffects import boostModListByReq, increase
def carrierCaldariLeadershipMaxGroupActive4(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Carrier")
    boostModListByReq(fitting.modules, "maxGroupActive", "carrierCaldariBonus4",
                      lambda mod: mod.group.name == "Gang Coordinator",
                      self.item, helper = increase, extraMult = level)
