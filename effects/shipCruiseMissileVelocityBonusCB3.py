#Item: Golem [Ship]
#Item: Raven [Ship]
#Item: Raven Navy Issue [Ship]
#Item: Raven State Issue [Ship]
#Item: Widow [Ship]
from customEffects import boostAmmoListBySkillReq
def shipCruiseMissileVelocityBonusCB3(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Battleship")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCB3",
                            lambda skill: skill.name == "Cruise Missiles",
                            self.item, extraMult = level)
