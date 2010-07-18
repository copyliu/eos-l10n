#Item: Hardwiring - Zainou 'Snapshot' ZMT1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMT500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusTorpedo(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Torpedoes", self.item)