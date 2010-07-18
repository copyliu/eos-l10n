#Variations of item: Executioner (2 of 3) [Ship]
#Variations of item: Magnate (3 of 4) [Ship]
#Variations of item: Punisher (2 of 3) [Ship]
#Item: Crucifier [Ship]
from customEffects import boostModListBySkillReq
def shipEnergyTCapNeedBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonus2AF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)