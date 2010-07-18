#Item: Hardwiring - Zainou 'Snapshot' ZMU1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMU2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMU500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusCruise3(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Cruise Missiles", self.item)