#Item: Claw
from customEffects import boostModListBySkillReq
def interceptor2ProjectileTracking(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusInterceptor2",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)