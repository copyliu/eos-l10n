#Used by: Ship: Thanatos
#               Nyx
from customEffects import boostModListBySkillReq
def carrierGallenteArmorShieldTransferRange3(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    boostModListBySkillReq(fitting.modules, "shieldTransferRange", "carrierGallenteBonus3",
                           lambda skill: skill.name == "Capital Shield Emission Systems",
                           self.item, extraMult = level)
    boostModListBySkillReq(fitting.modules, "maxRange", "carrierGallenteBonus3",
                           lambda skill: skill.name == "Capital Remote Armor Repair Systems",
                           self.item, extraMult = level)
