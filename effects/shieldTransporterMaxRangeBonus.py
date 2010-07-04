#Used by: Ship: Osprey
from customEffects import boostModListByReq
def shieldTransporterMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "shieldTransferRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Shield Transporter",
                      self.item)
