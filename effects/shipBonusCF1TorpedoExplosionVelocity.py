#Item: Manticore [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusCF1TorpedoExplosionVelocity(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonusCF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)