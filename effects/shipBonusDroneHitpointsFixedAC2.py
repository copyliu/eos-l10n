#Used by: Ship: Arbitrator
#               Pilgrim
#               Curse
from customEffects import boostDroneListByReq
def shipBonusDroneHitpointsFixedAC2(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Cruiser")
    boostDroneListByReq(fitting.drones, ("shieldCapacity", "armorHP", "hp"), "shipBonusAC2",
                        lambda drone: True, self.item, extraMult = level)