#Item: Crow
from customEffects import boostAmmoListBySkillReq
def interceptor2MissileVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "eliteBonusInterceptor2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)