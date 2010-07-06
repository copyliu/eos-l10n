#Used by: Ship: Hound
from customEffects import boostAmmoListBySkillReq
def shipBonusMF1TorpedoFlightTime(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "shipBonusMF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)