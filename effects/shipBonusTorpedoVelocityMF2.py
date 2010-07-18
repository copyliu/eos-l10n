#Item: Hound
from customEffects import boostAmmoListBySkillReq
def shipBonusTorpedoVelocityMF2(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusMF2",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)