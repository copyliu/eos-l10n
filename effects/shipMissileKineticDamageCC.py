#Item: Caracal
#Item: Caracal Navy Issue
#Item: Cerberus
#Item: Onyx
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusCC",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
