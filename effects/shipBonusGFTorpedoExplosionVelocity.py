#Item: Nemesis
from customEffects import boostAmmoListBySkillReq
def shipBonusGFTorpedoExplosionVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonusGF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)