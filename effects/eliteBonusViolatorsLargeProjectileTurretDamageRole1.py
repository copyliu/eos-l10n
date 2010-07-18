#Item: Vargur [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusViolatorsLargeProjectileTurretDamageRole1(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusViolatorsRole1",
                           lambda skill: skill.name == "Large Projectile Turret", self.item)