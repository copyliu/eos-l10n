#Items from group: Interdictor (4 of 4)
from customEffects import boostModListByReq
def eliteBonusInterdictorsInterdictionSphereLauncherReactivationDelay2(self, fitting):
    skill, level = fitting.getCharSkill("Interdictors")
    boostModListByReq(fitting.modules, "moduleReactivationDelay", "eliteBonusInterdictors2",
                      lambda mod: mod.group.name == "Interdiction Sphere Launcher",
                      self.item, extraMult = level)