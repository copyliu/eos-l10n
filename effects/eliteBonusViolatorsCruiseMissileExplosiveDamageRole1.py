#Used by: Ship: Golem
from customEffects import boostAmmoListBySkillReq
def eliteBonusViolatorsCruiseMissileExplosiveDamageRole1(self, fitting):
    boostAmmoListBySkillReq(fitting.modules, "explosiveDamage", "eliteBonusViolatorsRole1",
                       lambda skill: skill.name == "Cruise Missiles", self.item)