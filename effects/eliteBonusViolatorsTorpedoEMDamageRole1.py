#Item: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsTorpedoEMDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Torpedoes", self.item)