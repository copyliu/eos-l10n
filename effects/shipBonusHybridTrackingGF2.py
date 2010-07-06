#Used by: Ship: Tristan
#               Federation Navy Comet
#               Ares
from customEffects import boostModListBySkillReq
def shipBonusHybridTrackingGF2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "trackingSpeed", "shipBonusGF2",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
