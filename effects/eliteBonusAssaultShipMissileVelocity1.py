#Used by: Ship: Hawk
from customEffects import boostAmmoListBySkillReq
def eliteBonusAssaultShipMissileVelocity1(self, fitting):
     skill, level = fitting.getCharSkill("Assault Ships")
     boostAmmoListBySkillReq(fitting.modules, "maxVelocity", "eliteBonusGunship1",
                        lambda skill: skill.name == "Missile Launcher Operation",
                        self.item, extraMult = level)