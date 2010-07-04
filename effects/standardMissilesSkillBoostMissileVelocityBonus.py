#Used by: Skill: Defender Missiles
from customEffects import boostAmmoListByReq
def standardMissilesSkillBoostMissileVelocityBonus(self, fitting, level):
    boostAmmoListByReq(fitting.modules, "maxVelocity", "missileVelocityBonus",
                       lambda ammo: self.item in ammo.requiredSkills,
                       self.item, extraMult = level)