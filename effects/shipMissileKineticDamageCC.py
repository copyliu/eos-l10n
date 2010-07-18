#Item: Caracal [Ship]
#Item: Caracal Navy Issue [Ship]
#Item: Cerberus [Ship]
#Item: Onyx [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusCC",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
