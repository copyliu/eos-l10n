#Item: Proteus Offensive - Drone Synthesis Projector
from customEffects import boostDroneListByReq
def subsystemBonusGallenteOffensiveDroneHP(self, fitting, state):
    skill, level = fitting.getCharSkill("Gallente Offensive Systems")
    boostDroneListByReq(fitting.drones, ("shieldCapacity", "armorHP", "hp"),
                        "subsystemBonusGallenteOffensive", lambda drone: True,
                        self.item, extraMult = level)