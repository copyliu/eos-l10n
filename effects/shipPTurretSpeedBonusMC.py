#Used by: Ship: Bellicose
#               Stabber
#               Stabber Fleet Issue
#               Rupture
#               Scythe Fleet Issue
#               Rapier
#               Huginn
#               Broadsword
#               Vagabond
#               Muninn
from customEffects import boostModListBySkillReq
def shipPTurretSpeedBonusMC(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Cruiser")
    boostModListBySkillReq(fitting.modules, "speed", "shipBonusMC",
                           lambda skill: skill.name == "Medium Projectile Turret",
                           self.item, extraMult = level)
