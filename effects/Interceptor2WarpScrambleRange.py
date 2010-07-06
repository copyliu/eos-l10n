#Used by: Ship: Raptor
#               Malediction
#               Stiletto
#               Ares
from customEffects import boostModListByReq
def Interceptor2WarpScrambleRange(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusInterceptor2",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)