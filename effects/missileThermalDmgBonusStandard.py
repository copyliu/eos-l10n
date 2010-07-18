#Item: Hardwiring - Zainou 'Snapshot' ZMN1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMN500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileThermalDmgBonusStandard(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Standard Missiles", self.item)