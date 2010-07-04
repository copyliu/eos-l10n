#Used by: Ship: Rorqual
from customEffects import boostModListBySkillReq
def oreCapitalShipShieldTransferRange(self, fitting):
    skill, level = fitting.getCharSkill("Capital Industrial Ships")
    boostModListBySkillReq(fitting.modules, "shieldTransferRange", "shipBonusORECapital3",
                           lambda skill: skill.name == "Capital Shield Emission Systems",
                           self.item, extraMult = level)
