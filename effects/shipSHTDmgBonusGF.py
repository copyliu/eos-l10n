#Items from category: Ship (10 of 245)
#Items from market group: Ships > Assault Ships > Gallente (2 of 2)
#Items from market group: Ships > Interceptors > Gallente (2 of 2)
from customEffects import boostModListBySkillReq
def shipSHTDmgBonusGF(self, fitting):
    skill, level = fitting.getCharSkill("Gallente Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusGF",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)
