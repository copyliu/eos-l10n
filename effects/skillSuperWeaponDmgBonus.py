#Item: Doomsday Operation [Skill]
from customEffects import boostModListByReq
def skillSuperWeaponDmgBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Super Weapon" and "emDamage" in mod.attributes,
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Super Weapon" and "thermalDamage" in mod.attributes,
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Super Weapon" and "kineticDamage" in mod.attributes,
                      self.item, extraMult = level)
    boostModListByReq(fitting.modules, "explosiveDamage", "damageMultiplierBonus",
                      lambda mod: mod.group.name == "Super Weapon" and "explosiveDamage" in mod.attributes,
                      self.item, extraMult = level)