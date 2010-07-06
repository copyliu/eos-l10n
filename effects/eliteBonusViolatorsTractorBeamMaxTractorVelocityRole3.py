#Used by: Ship: Paladin
#               Kronos
#               Vargur
#               Golem
from customEffects import boostModListByReq
def eliteBonusViolatorsTractorBeamMaxTractorVelocityRole3(self, fitting):
    boostModListByReq(fitting.modules, "maxTractorVelocity", "eliteBonusViolatorsRole3",
                      lambda mod: mod.group.name == "Tractor Beam", self.item)
