#Used by: Ship: Thanatos
#               Nyx
from customEffects import boostDroneListBySkillReq
def carrierGallenteDroneOwnDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    boostDroneListBySkillReq(fitting.drones, "damageMultiplier", "carrierGallenteBonus2",
                                      lambda skill: skill.name == "Fighters",
                                      self.item, extraMult = level)
