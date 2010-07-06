#Used by: Ship: Nidhoggur
#               Hel
from customEffects import boostModListBySkillReq
def carrierMinmatarArmorShieldTransferRange3(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Carrier")
    boostModListBySkillReq(fitting.modules, "shieldTransferRange", "carrierMinmatarBonus3",
                           lambda skill: skill.name == "Capital Shield Emission Systems",
                           self.item, extraMult = level)
    boostModListBySkillReq(fitting.modules, "maxRange", "carrierMinmatarBonus3",
                           lambda skill: skill.name == "Capital Remote Armor Repair Systems",
                           self.item, extraMult = level)
