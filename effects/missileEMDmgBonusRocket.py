#Item: Hardwiring - Zainou 'Snapshot' ZMR1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)