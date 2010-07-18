#Item: Rook
from customEffects import boostAmmoListBySkillReq
def eliteReconBonusHeavyMissileVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "eliteBonusReconShip1",
                            lambda skill: skill.name == "Heavy Missiles",
                            self.item, extraMult = level)