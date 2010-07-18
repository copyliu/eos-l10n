#Item: Defender Missiles
from customEffects import boostAmmoListByReq
def standardMissilesSkillBoostMissileVelocityBonus(self, fitting, level):
    boostAmmoListByReq(fitting.modules, "maxVelocity", "missileVelocityBonus",
                       lambda charge: self.item in charge.requiredSkills,
                       self.item, extraMult = level)