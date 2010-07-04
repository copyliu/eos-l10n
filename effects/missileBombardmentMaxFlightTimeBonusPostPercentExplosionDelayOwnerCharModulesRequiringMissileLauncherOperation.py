#Used by: Skill: Missile Bombardment
#         Item : Rocket Fuel Cache Partition
from customEffects import boostAmmoListBySkillReq
def missileBombardmentMaxFlightTimeBonusPostPercentExplosionDelayOwnerCharModulesRequiringMissileLauncherOperation(self, fitting, state = None, level = 1):
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "maxFlightTimeBonus",
                           lambda skill: skill.name == "Missile Launcher Operation",
                           self.item, extraMult = level)