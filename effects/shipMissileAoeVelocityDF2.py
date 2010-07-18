#Item: Heretic
from customEffects import boostAmmoListBySkillReq
def shipMissileAoeVelocityDF2(self, fitting):
    skill, level = fitting.getCharSkill("Destroyers")
    boostAmmoListBySkillReq(fitting.modules, "aoeVelocity", "shipBonusDF2",
                            lambda skill: skill.name == "Missile Launcher Operation",
                            self.item, extraMult = level)