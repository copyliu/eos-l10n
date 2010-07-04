#Used by: Ship: Manticore
from customEffects import boostAmmoListBySkillReq
def eliteBonusCoverOpsBombKineticDmg1(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "eliteBonusCoverOps1",
                       lambda skill: skill.name == "Bomb Deployment",
                       self.item, extraMult = level)