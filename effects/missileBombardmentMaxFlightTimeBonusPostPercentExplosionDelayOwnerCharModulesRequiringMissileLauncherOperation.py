#Variations of item: Large Rocket Fuel Cache Partition I (2 of 2) [Module]
#Variations of item: Medium Rocket Fuel Cache Partition I (2 of 2) [Module]
#Variations of item: Small Rocket Fuel Cache Partition I (2 of 2) [Module]
#Item: Hardwiring - Zainou 'Deadeye' ZMC10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMC100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZMC1000 [Implant]
#Item: Missile Bombardment [Skill]
from customEffects import boostAmmoListBySkillReq
def missileBombardmentMaxFlightTimeBonusPostPercentExplosionDelayOwnerCharModulesRequiringMissileLauncherOperation(self, fitting, state = None, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "maxFlightTimeBonus",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)