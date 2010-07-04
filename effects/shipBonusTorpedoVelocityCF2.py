#Used by: Ship: Manticore
from customEffects import boostAmmoListBySkillReq
def shipBonusTorpedoVelocityCF2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCF2",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)