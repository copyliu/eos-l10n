#Used by: Ship: Archon
#               Aeon
from customEffects import boostModListBySkillReq
def carrierAmarrArmorEnergyTransferRange3(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Carrier")
    boostModListBySkillReq(fitting.modules, "maxRange", "carrierAmarrBonus3",
                           lambda skill: skill.name == "Capital Remote Armor Repair Systems",
                           self.item, extraMult = level)
    boostModListBySkillReq(fitting.modules, "powerTransferRange", "carrierAmarrBonus3",
                           lambda skill: skill.name == "Capital Energy Emission Systems",
                           self.item, extraMult = level)
