#Used by: Ship: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsCruiseMissileThermalDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "thermalDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Cruise Missiles", self.item)