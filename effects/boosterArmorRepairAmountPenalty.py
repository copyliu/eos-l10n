#Used by: Item: Sooth Sayer Booster
#               Mindflood Booster
#               Drop Booster
type = "boosterSideEffect"
from customEffects import boostModListByReq
def boosterArmorRepairAmountPenalty(self, fitting):
    boostModListByReq(fitting.modules, "armorDamageAmount", "boosterArmorRepairAmountPenalty",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item)