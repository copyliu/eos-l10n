#Used by: Ship: Viator
from customEffects import boostModListByReq
def eliteIndustrialArmorRepairDurationElite2(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boostModListByReq(fitting.modules, "duration", "eliteBonusIndustrial2",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)