#Item: Explosive Shield Compensation
from customEffects import boostModListByReq
def explosiveShieldCompensationHardeningBonusGroupShieldAmp(self, fitting, level):
    boostModListByReq(fitting.modules, "explosiveDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Shield Amplifier",
                      self.item, extraMult = level)