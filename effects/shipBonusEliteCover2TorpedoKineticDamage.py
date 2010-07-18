#Item: Manticore [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusEliteCover2TorpedoKineticDamage(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "eliteBonusCoverOps2",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)
