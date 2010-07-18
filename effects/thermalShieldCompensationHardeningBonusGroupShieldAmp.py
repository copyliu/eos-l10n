#Item: Thermic Shield Compensation [Skill]
from customEffects import boostModListByReq
def thermalShieldCompensationHardeningBonusGroupShieldAmp(self, fitting, level):
    boostModListByReq(fitting.modules, "thermalDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Shield Amplifier",
                      self.item, extraMult = level)