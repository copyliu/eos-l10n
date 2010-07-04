#Used by: Ship: Purifier
from customEffects import boostAmmoListBySkillReq
def shipBonusAF1TorpedoExplosionVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonusAF",
                            lambda skill: skill.name == "Torpedoes",
                            self.item, extraMult = level)