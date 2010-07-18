#Item: Fuel Conservation
from customEffects import boostModListBySkillReq
def fuelConservationCapNeedBonusPostPercentCapacitorNeedLocationShipModulesRequiringAfterburner(self, fitting, level):
    boostModListBySkillReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                           lambda skill: skill.name == "Afterburner",
                           self.item, extraMult = level)