#Item: Hound [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusCoverOpsBombExplosiveDmg1(self, fitting):
    skill, level = fitting.getCharSkill("Covert Ops")
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "eliteBonusCoverOps1",
                       lambda skill: skill.name == "Bomb Deployment",
                       self.item, extraMult = level)