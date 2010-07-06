#Used by: Ship: Executioner
#               Impairor
#               Punisher
#               Crucifier
#               Crusader
#               Retribution
#               Gold Magnate
#               Silver Magnate
#               Amarr Navy Slicer
#               Magnate
from customEffects import boostModListBySkillReq
def shipEnergyTCapNeedBonusAF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "shipBonus2AF",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)