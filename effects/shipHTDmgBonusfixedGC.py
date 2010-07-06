#Used by: Ship: Celestis
#               Thorax
#               Vexor
#               Vexor Navy Issue
#               Guardian-Vexor
#               Exequror Navy Issue
#               Arazu
#               Lachesis
#               Phobos
#               Deimos
#               Ishtar
#               Adrestia
from customEffects import boostModListBySkillReq
def shipHTDmgBonusfixedGC(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Cruiser")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGC",
                           lambda skill: skill.name == "Medium Hybrid Turret",
                           self.item, extraMult = level)
