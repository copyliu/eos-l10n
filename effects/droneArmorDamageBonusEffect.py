#Used by: Ship: Guardian
#               Oneiros
from customEffects import boostDroneListByReq
def droneArmorDamageBonusEffect(self, fitting):
    skill, level = fitting.getCharSkill(self.item.race.capitalize() + " Cruiser")
    boostDroneListByReq(fitting.drones, "armorDamageAmount", "droneArmorDamageAmountBonus",
                        lambda drone: "Armor Maintenance Bot" in drone.name,
                        self.item, extraMult = level)
