#Item: Hardwiring - Zainou 'Snapshot' ZME1000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZME2000 [Implant]
#Item: Hardwiring - Zainou 'Snapshot' ZME500 [Implant]
from customEffects import boostAmmoListBySkillReq
def missileEMDmgBonusHAM(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "damageMultiplierBonus",
                       lambda skill: skill.name == "Heavy Assault Missiles",
                       self.item)