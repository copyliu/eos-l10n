#Item: Rorqual [Ship]
from customEffects import boostDroneListByReq
def shipBonusORECapShipDroneDmgBonus(self, fitting):
    skill, level = fitting.getCharSkill("Capital Industrial Ships")
    boostDroneListByReq(fitting.drones, "damageMultiplier", "shipBonusORECapital4",
                        lambda drone: drone.group.name == "Combat Drone",
                        self.item, extraMult = level)
