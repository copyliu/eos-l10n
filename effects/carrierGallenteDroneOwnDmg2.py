#Items from market group: Ships > Carriers > Gallente (2 of 2)
from customEffects import boostDroneListBySkillReq
def carrierGallenteDroneOwnDmg2(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Carrier")
    boostDroneListBySkillReq(fitting.drones, "damageMultiplier", "carrierGallenteBonus2",
                                      lambda skill: skill.name == "Fighters",
                                      self.item, extraMult = level)
