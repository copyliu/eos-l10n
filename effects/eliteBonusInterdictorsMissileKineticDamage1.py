#Item: Flycatcher
from customEffects import boostAmmoListBySkillReq
def eliteBonusInterdictorsMissileKineticDamage1(self, fitting):
    skill, level = fitting.getCharSkill("Interdictors")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "eliteBonusInterdictors1",
                            lambda skill: skill.name == "Rockets" or \
                            skill.name == "Standard Missiles",
                            self.item, extraMult = level)