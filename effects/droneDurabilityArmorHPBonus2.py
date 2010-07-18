#Item: Drone Durability [Skill]
from customEffects import boostDroneListBySkillReq
def droneDurabilityArmorHPBonus2(self, fitting, level):
    boostDroneListBySkillReq(fitting.drones, "armorHP", "armorHpBonus",
                             lambda skill: skill.name == "Drones", self.item, extraMult = level)
