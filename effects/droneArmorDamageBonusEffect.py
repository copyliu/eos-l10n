#Items from group: Logistics (2 of 4)
from customEffects import boostDroneListByReq
def droneArmorDamageBonusEffect(self, fitting):
    skill, level = fitting.getCharSkill(self.item.race.capitalize() + " Cruiser")
    boostDroneListByReq(fitting.drones, "armorDamageAmount", "droneArmorDamageAmountBonus",
                        lambda drone: "Armor Maintenance Bot" in drone.name,
                        self.item, extraMult = level)
