#Used by: Ship: Exequror
from customEffects import boostModListByReq
def armorRepairProjectorMaxRangeBonus(self, fitting):
    boostModListByReq(fitting.modules, "maxRange", "maxRangeBonus",
                      lambda mod: mod.group.name == "Armor Repair Projector", self.item)