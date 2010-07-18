#Items from category: Ship (8 of 245)
#Variations of item: Magnate (3 of 4) [Ship]
from customEffects import boostModListBySkillReq
def shipEnergyTCapNeedBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonus2AF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)