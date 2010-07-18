#Item: Rorqual
from customEffects import boostModListByReq
def rorqualSurveyScannerRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "surveyScannerRangeBonus",
                      lambda mod: mod.group.name == "Survey Scanner", self.item)