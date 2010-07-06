#Used by: Skill: Fighter Bombers
from customEffects import boostDroneListAmmoBySkillReq
def fighterBomberExplosiveDamageBonus2(self, fitting, level):
    boostDroneListAmmoBySkillReq(fitting.drones, "explosiveDamage", "damageMultiplierBonus",
                                 lambda skill: skill.name == "Fighter Bombers",
                                 self.item, extraMult = level)
