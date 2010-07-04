#Used by: Ship: Claymore
from customEffects import boostModListBySkillReq
def eliteBonusCommandShipProjectileTrackingCS1(self, fitting):
    skill, level = fitting.getCharSkill("Command Ships")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "eliteBonusCommandShips1",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)