#Items from group: Effect Beacon (6 of 38) [Celestial]
type= "projected"
from customEffects import boostModListByReq, multiply
def systemArmorRepairAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "armorDamageAmount", "armorDamageAmountMultiplier",
             lambda mod: mod.group.name == "Armor Repair Unit",
             self.item, helper = multiply)