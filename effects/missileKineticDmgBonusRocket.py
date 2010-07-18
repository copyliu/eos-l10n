#Item: Hardwiring - Zainou 'Snapshot' ZMR1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMR500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusRocket(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Rockets", self.item)