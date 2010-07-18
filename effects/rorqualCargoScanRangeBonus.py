#Item: Rorqual
from customEffects import boostModListByReq
def rorqualCargoScanRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "cargoScannerRangeBonus",
                      lambda mod: mod.group.name == "Cargo Scanner", self.item)