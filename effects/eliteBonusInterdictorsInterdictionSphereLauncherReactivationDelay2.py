#Used by: Ship: Heretic
#               Sabre
#               Eris
#               Flycatcher
from customEffects import boostModListByReq
def eliteBonusInterdictorsInterdictionSphereLauncherReactivationDelay2(self, fitting):
    skill, level = fitting.getCharSkill("Interdictors")
    boostModListByReq(fitting.modules, "moduleReactivationDelay", "eliteBonusInterdictors2",
                      lambda mod: mod.group.name == "Interdiction Sphere Launcher",
                      self.item, extraMult = level)