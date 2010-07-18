#Item: Nyx
from customEffects import boostDroneListAmmoBySkillReq
def carrierGallente1BomberDroneMissileDamageMultiplierBonus(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    for damageType in ("em", "kinetic", "thermal", "explosive"):
        boostDroneListAmmoBySkillReq(fitting.drones, damageType + "Damage", "carrierGallenteBonus2",
                                     lambda skill: skill.name == "Fighter Bombers",
                                     self.item, extraMult = level)
