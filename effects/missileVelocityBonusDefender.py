#Used by: Item: Hardwiring - 'Snapshot' ZMDX
from customEffects import boostAmmoListBySkillReq
def missileVelocityBonusDefender(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "missileVelocityBonus",
                       lambda skill: skill.name == "Defender Missiles")