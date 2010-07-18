#Item: Myrmidon
from customEffects import boostDroneListByReq
def shipBonusDroneDamageMultiplierBC1(self, fitting):
    skill, level = fitting.getCharSkill("Battlecruisers")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusBC1",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)