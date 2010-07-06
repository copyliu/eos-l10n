#Used by: Ship: Caracal
#               Caracal Navy Issue
#               Cerberus
from customEffects import boostAmmoListBySkillReq
def shipMissileLightVelocityBonusCC2(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "shipBonusCC2",
                            lambda skill: skill.name == "Standard Missiles",
                            self.item, extraMult = level)
