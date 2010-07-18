#Items from category: Ship (10 of 245)
from customEffects import boostModListBySkillReq
def shipPTurretSpeedBonusMC(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusMC",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
