#Used by: Ship: Slasher
#               Rifter
#               Republic Fleet Firetail
#               Cheetah
#               Stilleto
#               Claw
#               Jaguar
#               Wolf
from customEffects import boostModListBySkillReq
def shipPDmgBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMF",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
