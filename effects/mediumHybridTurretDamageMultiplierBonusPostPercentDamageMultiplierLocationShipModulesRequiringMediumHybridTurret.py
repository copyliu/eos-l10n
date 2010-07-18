#Item: Hardwiring - Zainou 'Deadeye' ZGM10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGM100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGM1000 [Implant]
#Item: Medium Hybrid Turret [Skill]
from customEffects import boostModListBySkillReq
def mediumHybridTurretDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringMediumHybridTurret(self, fitting, level = 1):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "damageMultiplierBonus",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)