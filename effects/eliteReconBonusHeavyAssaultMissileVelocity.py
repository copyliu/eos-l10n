#Item: Rook [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteReconBonusHeavyAssaultMissileVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "eliteBonusReconShip1",
                      lambda skill: skill.name == "Heavy Assault Missiles",
                      self.item, extraMult = level)