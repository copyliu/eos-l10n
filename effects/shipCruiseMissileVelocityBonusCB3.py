#Used by: Ship: Raven
#               Raven Navy Issue
#               Raven State Issue
#               Widow
#               Golem
from customEffects import boostAmmoListBySkillReq
def shipCruiseMissileVelocityBonusCB3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCB3",
                            lambda skill: skill.name == "Cruise Missiles",
                            self.item, extraMult = level)
