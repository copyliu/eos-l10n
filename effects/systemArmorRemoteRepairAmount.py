#Items from group: Effect Beacon (6 of 38) [Celestial]
type= "projected"
from customEffects import boostModListByReq, multiply
def systemArmorRemoteRepairAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "armorDamageAmount", "armorDamageAmountMultiplier",
             lambda mod: mod.group.name == "Armor Repair Projector",
             self.item, helper = multiply)