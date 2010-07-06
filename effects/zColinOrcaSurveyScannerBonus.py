#Used by: Ship: Orca
from customEffects import boostModListByReq
def zColinOrcaSurveyScannerBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "shipOrcaSurveyScannerBonus",
                      lambda mod: mod.group.name == "Survey Scanner", self.item)