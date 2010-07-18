#Items from group: Assault Ship (3 of 8)
#Items from market group: Ships > Assault Ships > Gallente (2 of 2)
from customEffects import boostModListBySkillReq
def eliteBonusGunshipHybridOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusGunship1",
                           lambda skill: skill.name == "Small Hybrid Turret",
                           self.item, extraMult = level)