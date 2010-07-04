#Used by: Item: Cataclysmic Variable Effect Beacon
type= "projected"
from customEffects import boostModListByReq, multiply
def systemArmorRepairAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "armorDamageAmount", "armorDamageAmountMultiplier",
             lambda mod: mod.group.name == "Armor Repair Unit",
             self.item, helper = multiply)