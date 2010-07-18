#Item: Thrasher
from customEffects import boostModListBySkillReq
def smallProjectileMaxRangeBonus(self, fitting):
    boostModListBySkillReq(fitting.modules, "maxRange", "maxRangeBonus",
                           lambda skill: skill.name == "Small Projectile Turret",
                           self.item)