#Variations of item: Caracal (3 of 3) [Ship]
#Item: Onyx [Ship]
from customEffects import boostAmmoListBySkillReq
def shipMissileKineticDamageCC(self, fitting):
    skill, level = fitting.getCharSkill("Caldari Cruiser")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "shipBonusCC",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)
