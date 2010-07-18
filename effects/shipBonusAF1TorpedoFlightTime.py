#Item: Purifier
from customEffects import boostAmmoListBySkillReq
def shipBonusAF1TorpedoFlightTime(self, fitting):
    skill, level = fitting.getCharSkill("Amarr Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "shipBonusAF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)