#Used by: Ship: Osprey Navy Issue
#               Caracal
#               Caracal Navy Issue
#               Cerberus
from customEffects import boostAmmoListBySkillReq
def shipMissileAssaultMissileVelocityBonusCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCC2",
                            lambda skill: skill.name == "Heavy Assault Missiles",
                            self.item, extraMult = level)
