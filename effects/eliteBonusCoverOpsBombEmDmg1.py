#Item: Purifier [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusCoverOpsBombEmDmg1(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "eliteBonusCoverOps1",
                       lambda skill: skill.name == "Bomb Deployment",
                       self.item, extraMult = level)