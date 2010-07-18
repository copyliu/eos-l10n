#Item: Hardwiring - Zainou 'Snapshot' ZMN1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)