#Used by: Ship: Vexor
#               Vexor Navy Issue
#               Gila
#               Ishtar
from customEffects import boostDroneListByReq
def shipBonusDroneHitpointsGC2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostDroneListByReq(fitting.drones, ("shieldCapacity", "armorHP", "hp"), "shipBonusGC2",
                        lambda mod: True, self.item, extraMult = level)
