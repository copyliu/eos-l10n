#Item: Nemesis [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusCoverOpsBombThermalDmg1(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "eliteBonusCoverOps1",
                       lambda skill: skill.name == "Bomb Deployment",
                       self.item, extraMult = level)