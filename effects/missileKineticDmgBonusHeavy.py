#Item: Hardwiring - Zainou 'Snapshot' ZMH1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMH2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZMH500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileKineticDmgBonusHeavy(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Missiles", self.item)