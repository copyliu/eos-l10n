#Item: Orca
from customEffects import boostModListBySkillReq
def zColinOrcaForemanModBonus(self, fitting):
    skill, level = fitting.getCharSkill("Industrial Command Ships")
    boostModListBySkillReq(fitting.modules, "commandBonus", "shipOrcaCargoBonusOrca1",
                           lambda skill: skill.name == "Mining Director",
                           self.item, extraMult = level)
