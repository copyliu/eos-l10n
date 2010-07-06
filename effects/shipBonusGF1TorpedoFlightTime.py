#Used by: Ship: Nemesis
from customEffects import boostAmmoListBySkillReq
def shipBonusGF1TorpedoFlightTime(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "shipBonusGF",
                       lambda skill: skill.name == "Torpedoes",
                       self.item, extraMult = level)