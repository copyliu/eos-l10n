#Variations of item: Large Rocket Fuel Cache Partition I (2 of 2)
#Variations of item: Medium Rocket Fuel Cache Partition I (2 of 2)
#Variations of item: Small Rocket Fuel Cache Partition I (2 of 2)
#Item: Hardwiring - Zainou 'Deadeye' ZMC10
#Item: Hardwiring - Zainou 'Deadeye' ZMC100
#Item: Hardwiring - Zainou 'Deadeye' ZMC1000
#Item: Missile Bombardment
from customEffects import boostAmmoListBySkillReq
def missileBombardmentMaxFlightTimeBonusPostPercentExplosionDelayOwnerCharModulesRequiringMissileLauncherOperation(self, fitting, state = None, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "maxFlightTimeBonus",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)