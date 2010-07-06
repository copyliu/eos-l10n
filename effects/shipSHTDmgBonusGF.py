#Used by: Ship: Velator
#               Maulus
#               Atron
#               Incursus
#               Tristan
#               Federation Navy Comet
#               Helios
#               Ares
#               Taranis
#               Ishkur
#               Enyo
from customEffects import boostModListBySkillReq
def shipSHTDmgBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGF",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
