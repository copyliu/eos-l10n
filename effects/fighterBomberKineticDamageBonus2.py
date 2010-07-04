#Used by: Skill: Fighter Bombers
from customEffects import boostDroneListAmmoBySkillReq
def fighterBomberKineticDamageBonus2(self, fitting, level):
    boostDroneListAmmoBySkillReq(fitting.drones, "kineticDamage", "damageMultiplierBonus",
                                 lambda skill: skill.name == "Fighter Bombers",
                                 self.item, extraMult = level)
