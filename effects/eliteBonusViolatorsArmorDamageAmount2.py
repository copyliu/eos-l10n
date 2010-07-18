#Items from group: Marauder (2 of 4) [Ship]
from customEffects import boostModListByReq
def eliteBonusViolatorsArmorDamageAmount2(self, fitting):
    skill, level = fitting.getCharSkill("Marauders")
    boostModListByReq(fitting.modules, "armorDamageAmount", "eliteBonusViolators2",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, extraMult = level)