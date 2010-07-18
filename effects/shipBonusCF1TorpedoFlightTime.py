#Item: Manticore [Ship]
from customEffects import boostAmmoListBySkillReq
def shipBonusCF1TorpedoFlightTime(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Frigate")
    boostAmmoListBySkillReq(fitting.modules, "explosionDelay", "shipBonusCF",
                            lambda skill: skill.name == "Torpedoes",
                            self.item, extraMult = level)