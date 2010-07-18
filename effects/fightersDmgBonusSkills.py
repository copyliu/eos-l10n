#Item: Fighters
from customEffects import boostDroneListByReq
def fightersDmgBonusSkills(self, fitting, level):
    boostDroneListByReq(fitting.drones, "damageMultiplier", "damageMultiplierBonus",
                        lambda drone: self.item in drone.requiredSkills,
                        self.item, extraMult = level)