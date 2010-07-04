#Used by: Ship: Paladin
#               Kronos
#               Vargur
#               Golem
from customEffects import boostModListByReq
def eliteBonusViolatorsTractorBeamMaxRangeRole2(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusViolatorsRole2",
                      lambda mod: mod.group.name == "Tractor Beam", self.item)
