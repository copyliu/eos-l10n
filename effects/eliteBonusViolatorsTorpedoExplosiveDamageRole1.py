#Item: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsTorpedoExplosiveDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Torpedoes", self.item)