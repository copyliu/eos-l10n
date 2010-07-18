#Item: Hardwiring - Zainou 'Snapshot' ZMT1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)