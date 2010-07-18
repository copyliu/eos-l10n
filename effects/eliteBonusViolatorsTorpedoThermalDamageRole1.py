#Item: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsTorpedoThermalDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Torpedoes", self.item)