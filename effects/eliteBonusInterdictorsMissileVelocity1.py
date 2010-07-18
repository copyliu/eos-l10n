#Item: Heretic [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusInterdictorsMissileVelocity1(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "eliteBonusInterdictors1",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)