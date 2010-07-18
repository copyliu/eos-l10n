#Item: Purifier [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusTorpedoVelocity2AF(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonus2AF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)