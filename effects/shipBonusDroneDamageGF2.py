from customEffects import boostDroneListByReq
def shipBonusDroneDamageGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusGF2",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)