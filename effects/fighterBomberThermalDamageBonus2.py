#Item: Fighter Bombers
from customEffects import boostDroneListAmmoBySkillReq
def fighterBomberThermalDamageBonus2(self, fitting, level):
    boostDroneListAmmoBySkillReq(fitting.drones, "thermalDamage", "damageMultiplierBonus",
                                 lambda skill: skill.name == "Fighter Bombers",
                                 self.item, extraMult = level)
