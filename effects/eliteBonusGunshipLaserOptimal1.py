#Item: Retribution
from customEffects import boostModListBySkillReq
def eliteBonusGunshipLaserOptimal1(self, fitting):
    skill, level = fitting.getCharSkill("Assault Ships")
    boostModListBySkillReq(fitting.modules, "maxRange", "eliteBonusGunship1",
                           lambda skill: skill.name == "Small Energy Turret",
                           self.item, extraMult = level)