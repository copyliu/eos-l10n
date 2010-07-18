#Item: Fighter Bombers
from customEffects import boostDroneListAmmoBySkillReq
def fighterBomberEmDamageBonus2(self, fitting, level):
    boostDroneListAmmoBySkillReq(fitting.drones, "emDamage", "damageMultiplierBonus",
                                 lambda skill: skill.name == "Fighter Bombers",
                                 self.item, extraMult = level)
