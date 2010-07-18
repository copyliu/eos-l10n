#Item: Paladin
from customEffects import boostModListBySkillReq
def eliteBonusViolatorsLargeEnergyTurretDamageRole1(self, fitting):
    boostModListBySkillReq(fitting.modules, "damageMultiplier", "eliteBonusViolatorsRole1",
                           lambda skill: skill.name == "Large Energy Turret",
                           self.item) 