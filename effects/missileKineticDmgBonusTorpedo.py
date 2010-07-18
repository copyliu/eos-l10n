#Item: Hardwiring - Zainou 'Snapshot' ZMT1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)