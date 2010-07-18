#Item: Eris
from customEffects import boostAmmoListBySkillReq
def eliteBonusInterdictorsMissileThermalDamage1(self, fitting):
    skill, level = fitting.getCharSkill("Interdictors")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "eliteBonusInterdictors1",
                            lambda skill: skill.name == "Rockets" or \
                            skill.name == "Standard Missiles",
                            self.item, extraMult = level)