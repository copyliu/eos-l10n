#Item: Erebus
from customEffects import boostModListBySkillReq
def titanGallenteHybridDamage1(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Titan")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "titanGallenteBonus1",
                           lambda skill: skill.name == "Capital Hybrid Turret",
                           self.item, extraMult = level)
