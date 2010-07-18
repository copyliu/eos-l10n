#Item: Golem
#Item: Raven
#Item: Raven Navy Issue
#Item: Raven State Issue
#Item: Widow
from customEffects import boostAmmoListBySkillReq
def shipTorpedosVelocityBonusCB3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCB3",
                            lambda skill: skill.name == "Torpedoes",
                            self.item, extraMult = level)
