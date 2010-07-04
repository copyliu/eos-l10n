#Used by: Ship: Hound
from customEffects import boostAmmoListBySkillReq
def shipBonusMF1TorpedoExplosionVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonusMF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)