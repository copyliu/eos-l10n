#Used by: Ship: Purifier
from customEffects import boostAmmoListBySkillReq
def shipBonusEliteCover2TorpedoEMDamage(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "eliteBonusCoverOps2",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)
