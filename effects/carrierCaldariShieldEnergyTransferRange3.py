#Used by: Ship: Chimera
#               Wyvern
from customEffects import boostModListBySkillReq
def carrierCaldariShieldEnergyTransferRange3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Carrier")
    boostModListBySkillReq(fitting.modules, "shieldTransferRange", "carrierCaldariBonus3",
                           lambda skill: skill.name == "Capital Shield Emission Systems",
                           self.item, extraMult = level)
    boostModListBySkillReq(fitting.modules, "powerTransferRange", "carrierCaldariBonus3",
                           lambda skill: skill.name == "Capital Energy Emission Systems",
                           self.item, extraMult = level)
