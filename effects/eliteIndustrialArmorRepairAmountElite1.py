#Items from group: Transport Ship (3 of 8) [Ship]
from customEffects import boostModListByReq
def eliteIndustrialArmorRepairAmountElite1(self, fitting):
    skill, level = fitting.getCharSkill("Transport Ships")
    boostModListByReq(fitting.modules, "armorDamageAmount", "eliteBonusIndustrial1",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)