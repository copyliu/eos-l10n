#Item: Nemesis [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusTorpedoVelocityGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusGF2",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)