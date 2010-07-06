#Used by: Ship: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsCruiseMissileKineticDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "kineticDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Cruise Missiles", self.item)