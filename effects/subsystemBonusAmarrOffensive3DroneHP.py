#Used by: Item: Legion Offensive - Drone Synthesis Projector
from customEffects import boostDroneListByReq
def subsystemBonusAmarrOffensive3DroneHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Amarr Offensive Systems")
    boostDroneListByReq(fitting.drones, ("shieldCapacity", "armorHP", "hp"),
                        "subsystemBonusAmarrOffensive3", lambda drone: True,
                        self.item, extraMult = level)