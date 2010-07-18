#Items from group: Interceptor (4 of 8) [Ship]
from customEffects import boostModListByReq
def Interceptor2WarpScrambleRange(self, fitting):
    skill, level = fitting.getCharSkill("Interceptors")
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusInterceptor2",
                      lambda mod: mod.group.name == "Warp Scrambler",
                      self.item, extraMult = level)