#Item: Kinetic Shield Compensation [Skill]
from customEffects import boostModListByReq
def kineticShieldCompensationHardeningBonusGroupShieldAmp(self, fitting, level):
    boostModListByReq(fitting.modules, "kineticDamageResistanceBonus", "hardeningBonus",
                      lambda mod: mod.group.name == "Shield Amplifier",
                      self.item, extraMult = level)