#Used by: Skill: Thermodynamics
from customEffects import boostModListByReq
def thermodynamicsSkillDamageBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "heatDamage", "thermodynamicsHeatDamage",
                           lambda mod: "heatDamage" in mod.attributes,
                           self.item, extraMult = level)
