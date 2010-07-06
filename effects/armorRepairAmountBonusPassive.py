#Used by: Item: Exile Booster
from customEffects import boostModListByReq
def armorRepairAmountBonusPassive(self, fitting):
    boostModListByReq(fitting.modules, "armorDamageAmount", "armorDamageAmountBonus",
                      lambda mod: mod.group.name == "Armor Repair Unit", self.item)