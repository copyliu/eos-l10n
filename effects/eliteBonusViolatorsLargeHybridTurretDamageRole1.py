#Item: Kronos [Ship]
from customEffects import boostModListBySkillReq
def eliteBonusViolatorsLargeHybridTurretDamageRole1(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusViolatorsRole1",
                           lambda skill: skill.name == "Large Hybrid Turret", self.item)