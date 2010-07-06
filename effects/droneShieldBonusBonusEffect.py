#Used by: Ship: Scimitar
#               Basilisk
from customEffects import boostDroneListByReq
def droneShieldBonusBonusEffect(self, fitting):
    skill, level = fitting.getCharSkill(self.item.race.capitalize() + " Cruiser")
    boostDroneListByReq(fitting.drones, "shieldBonus", "droneShieldBonusBonus",
                        lambda drone: "Shield Maintenance Bot" in drone.name,
                        self.item, extraMult = level)
