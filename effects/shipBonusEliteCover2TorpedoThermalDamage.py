#Item: Nemesis [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusEliteCover2TorpedoThermalDamage(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "eliteBonusCoverOps2",
                            lambda skill: skill.name == "Torpedoes",
                            self.item, extraMult = level)
