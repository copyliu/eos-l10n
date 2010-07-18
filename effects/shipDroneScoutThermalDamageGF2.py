#Item: Helios
from customEffects import boostDroneListBySkillReq
def shipDroneScoutThermalDamageGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostDroneListBySkillReq(fitting.drones, "thermalDamage", "shipBonusGF2",
                             lambda skill: skill.name == "Scout Drone Operation",
                             self.item, extraMult = level)