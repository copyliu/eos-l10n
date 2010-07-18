#Item: Hound [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusEliteCover2TorpedoExplosiveDamage(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "eliteBonusCoverOps2",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)
