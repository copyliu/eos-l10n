#Item: Golem [Ship]
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsTorpedoKineticDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Torpedoes", self.item)