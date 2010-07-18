#Variations of item: Caracal (3 of 3)
#Item: Osprey Navy Issue
from customEffects import boostAmmoListBySkillReq
def shipMissileAssaultMissileVelocityBonusCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCC2",
                            lambda skill: skill.name == "Heavy Assault Missiles",
                            self.item, extraMult = level)
