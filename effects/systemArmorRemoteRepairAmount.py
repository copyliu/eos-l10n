#Used by: Item: Cataclysmic Variable Effect Beacon
type= "projected"
from customEffects import boostModListByReq, multiply
def systemArmorRemoteRepairAmount(self, fitting, state):
    boostModListByReq(fitting.modules, "armorDamageAmount", "armorDamageAmountMultiplier",
             lambda mod: mod.group.name == "Armor Repair Projector",
             self.item, helper = multiply)