#Items from group: Marauder (4 of 4) [Ship]
from customEffects import boostModListByReq
def eliteBonusViolatorsTractorBeamMaxRangeRole2(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "eliteBonusViolatorsRole2",
                      lambda mod: mod.group.name == "Tractor Beam", self.item)
