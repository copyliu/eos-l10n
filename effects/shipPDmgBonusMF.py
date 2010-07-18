#Items from category: Ship (8 of 245)
#Items from market group: Ships > Assault Ships > Minmatar (2 of 2)
#Items from market group: Ships > Interceptors > Minmatar (2 of 2)
from customEffects import boostModListBySkillReq
def shipPDmgBonusMF(self, fitting):
    skill, level = fitting.getCharSkill("Minmatar Frigate")
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "shipBonusMF",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item, extraMult = level)
