#Item: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsCruiseMissileEMDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "emDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Cruise Missiles", self.item)